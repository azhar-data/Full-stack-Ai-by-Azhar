import numpy as np

np.set_printoptions(threshold=np.inf,linewidth=np.inf)

StartupName,Industry,FundingRounds,investment=np.genfromtxt(r"startup_growth_investment_data.csv",
                                                            delimiter=",",

                                                             usecols=(0,1,2,3),
                                                             dtype=None,unpack=True,
                                                             skip_header=1,
                                                             encoding='utf-8',
                                                             invalid_raise=False
                                                             )
print(StartupName)
print(Industry)
print(FundingRounds)
print(investment)

cleaned_FundingRounds = FundingRounds[~np.isnan(FundingRounds)]

value_sin=np.sin(FundingRounds)
value_cos=np.cos(FundingRounds)
value_tan=np.tan(FundingRounds)

print("value of sin:",value_sin)
print("the value of cos:",value_cos)
print("value of tan:",value_tan)

value_sinh=np.sinh(FundingRounds)
value_cosh=np.cosh(FundingRounds)
value_tanh=np.tanh(FundingRounds)

print("value of sinh:",value_sinh)
print("the value of cosh:",value_cosh)
print("value of tanh:",value_tanh)

addition=FundingRounds+investment
sub=FundingRounds-investment
devesion=FundingRounds/investment
multi=FundingRounds*investment
foolrdevision=FundingRounds//investment

print("addition of the value:",addition)
print("subtraction of the value:",sub)
print("devision of the value:",devesion)
print("multiply of the value:",multi)
print("devision floor of the value:",foolrdevision)

print("square of the value:",np.square(investment))
print("square rut of the value:",np.sqrt(investment))
print("power of the value:",np.power(investment,FundingRounds))
print("abs value:",np.abs(investment))


print(cleaned_FundingRounds)
