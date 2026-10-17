import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
 
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.metrics import (
    r2_score, mean_absolute_error, root_mean_squared_error,
    accuracy_score, classification_report, confusion_matrix,
    silhouette_score,
)
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
 
# =====================================================
# 1. LOAD DATA
# =====================================================
# utf-8-sig removes the hidden BOM character in the first column name
df = pd.read_csv('mobile data/smartphones.csv', encoding='utf-8-sig')
 
print(df.head())
print(df.shape)
df.info()
print(df.describe())
 
# =====================================================
# 2. CLEANING
# =====================================================
df = df.drop_duplicates().reset_index(drop=True)
print("\nMissing values before cleaning:\n", df.isnull().sum()[df.isnull().sum() > 0])
 
# Phones without fast charging have no fast_charging value -> 0 is logical
if 'fast_charging' in df.columns:
    no_fc = df['fast_charging_available'] == 0
    df.loc[no_fc & df['fast_charging'].isnull(), 'fast_charging'] = 0
 
# Remaining columns: median for numeric, mode for text
for col in df.columns:
    if df[col].isnull().any():
        if pd.api.types.is_numeric_dtype(df[col]):
            df[col] = df[col].fillna(df[col].median())
        else:
            df[col] = df[col].fillna(df[col].mode()[0])
 
print("\nMissing values after cleaning:", df.isnull().sum().sum())
 
# =====================================================
# 3. EDA
# =====================================================
plt.figure(figsize=(12, 8))
sns.heatmap(df.select_dtypes('number').corr(), annot=True, fmt='.2f', cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.tight_layout()
plt.show()
 
sns.histplot(df['price'], bins=40, kde=True)
plt.title('Price Distribution (right-skewed)')
plt.show()
 
sns.scatterplot(data=df, x='avg_rating', y='price')
plt.title('Rating vs Price')
plt.show()
 
top_brands = df['brand_name'].value_counts().head(10)
top_brands.plot(kind='bar')
plt.title('Top 10 Brands by Number of Phones')
plt.tight_layout()
plt.show()
 
# =====================================================
# 4. REGRESSION  (predict price)
# =====================================================
print("\n" + "=" * 50 + "\nREGRESSION\n" + "=" * 50)
 
X = df.drop(columns=['price', 'model'])
X = pd.get_dummies(X, columns=['brand_name', 'processor_brand', 'os'], drop_first=True)
y = np.log1p(df['price'])   # log transform because price is skewed
 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
 
reg = RandomForestRegressor(n_estimators=300, random_state=42, n_jobs=-1)
reg.fit(X_train, y_train)
 
# convert predictions back to real price scale
y_pred = np.expm1(reg.predict(X_test))
y_true = np.expm1(y_test)
 
print("R2   :", r2_score(y_true, y_pred))
print("MAE  :", mean_absolute_error(y_true, y_pred))
print("RMSE :", root_mean_squared_error(y_true, y_pred))
print("Train R2 (log scale):", reg.score(X_train, y_train))
print("CV R2 (log scale)   :", cross_val_score(reg, X, y, cv=5, scoring='r2').mean())
 
imp = pd.Series(reg.feature_importances_, index=X.columns).sort_values(ascending=False)
imp.head(10).plot(kind='barh', title='Top 10 Features for Price')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()
 
# Actual vs predicted
plt.scatter(y_true, y_pred, alpha=0.5)
plt.plot([y_true.min(), y_true.max()], [y_true.min(), y_true.max()], 'r--')
plt.xlabel('Actual Price')
plt.ylabel('Predicted Price')
plt.title('Actual vs Predicted')
plt.show()
 
# =====================================================
# 5. CLASSIFICATION  (predict price category)
# =====================================================
print("\n" + "=" * 50 + "\nCLASSIFICATION\n" + "=" * 50)
 
# 3 balanced classes: 0 = Budget, 1 = Mid-range, 2 = Premium
df['price_category'] = pd.qcut(df['price'], q=3, labels=[0, 1, 2]).astype(int)
 
# price must NOT be a feature here, otherwise it leaks the answer
Xc = df.drop(columns=['price', 'price_category', 'model'])
Xc = pd.get_dummies(Xc, columns=['brand_name', 'processor_brand', 'os'], drop_first=True)
yc = df['price_category']
 
Xc_train, Xc_test, yc_train, yc_test = train_test_split(
    Xc, yc, test_size=0.2, random_state=42, stratify=yc
)
 
clf = RandomForestClassifier(n_estimators=300, random_state=42, n_jobs=-1)
clf.fit(Xc_train, yc_train)
yc_pred = clf.predict(Xc_test)
 
print("Accuracy:", accuracy_score(yc_test, yc_pred))
print(classification_report(yc_test, yc_pred, target_names=['Budget', 'Mid-range', 'Premium']))
 
sns.heatmap(confusion_matrix(yc_test, yc_pred), annot=True, fmt='d', cmap='Blues',
            xticklabels=['Budget', 'Mid', 'Premium'],
            yticklabels=['Budget', 'Mid', 'Premium'])
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()
 
# =====================================================
# 6. CLUSTERING  (group similar phones)
# =====================================================
print("\n" + "=" * 50 + "\nCLUSTERING\n" + "=" * 50)
 
cluster_features = ['price', 'ram_capacity', 'internal_memory', 'battery_capacity',
                    'processor_speed', 'refresh_rate', 'primary_camera_rear', 'screen_size']
 
Xs = StandardScaler().fit_transform(df[cluster_features])
 
# Elbow + silhouette to choose k
inertias, sil_scores, ks = [], [], range(2, 9)
for k in ks:
    km = KMeans(n_clusters=k, random_state=42, n_init=10).fit(Xs)
    inertias.append(km.inertia_)
    sil_scores.append(silhouette_score(Xs, km.labels_))
 
fig, ax = plt.subplots(1, 2, figsize=(12, 4))
ax[0].plot(list(ks), inertias, marker='o')
ax[0].set_title('Elbow Method')
ax[0].set_xlabel('k')
ax[1].plot(list(ks), sil_scores, marker='o')
ax[1].set_title('Silhouette Score')
ax[1].set_xlabel('k')
plt.tight_layout()
plt.show()
 
best_k = list(ks)[int(np.argmax(sil_scores))]
print("Best k by silhouette:", best_k)
 
kmeans = KMeans(n_clusters=best_k, random_state=42, n_init=10)
df['cluster'] = kmeans.fit_predict(Xs)
 
print(df.groupby('cluster')[cluster_features].mean().round(2))
print(df['cluster'].value_counts())
 
# 2D visualisation with PCA
from sklearn.decomposition import PCA
pcs = PCA(n_components=2).fit_transform(Xs)
sns.scatterplot(x=pcs[:, 0], y=pcs[:, 1], hue=df['cluster'], palette='tab10')
plt.title('Phone Clusters (PCA view)')
plt.show()