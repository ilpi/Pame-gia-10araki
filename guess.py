import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import scipy.stats as st
import numpy as np


df = pd.read_csv('yo.csv', names = ['Age', 'Gender', 'tb', 'db', 'AAP', 'SAA', 'SGAA', 'TP', 'ALB', 'A-G', 'Ok'], delimiter=',')
changes = {'Male': 0, 'Female': 1}
df['Gender'] = df['Gender'].replace(changes)

nans = df.isnull().any(1).nonzero()[0]
if nans.all():
    df['A-G'] = df['A-G'].fillna(0)
plt.hist(df['A-G'])
plt.show()
#print(df.describe())
#mu = df['Age'].mean()
##s = np.random.normal(mu, sigma,100)
#print(np.mean(s)-np.std(s))
#matplotlib.style.use('ggplot')
#plt.hist(s)
#plt.show()
"""
def get_best_distribution(data):
    dist_names = ['alpha', 'anglit', 'arcsine', 'beta', 'betaprime', 'bradford', 'burr', 'cauchy', 'chi', 'chi2',
                  'cosine', 'dgamma', 'dweibull', 'erlang', 'expon', 'exponweib', 'exponpow', 'f', 'fatiguelife',
                  'fisk', 'foldcauchy', 'foldnorm', 'frechet_r', 'frechet_l', 'genlogistic', 'genpareto', 'genexpon',
                  'genextreme', 'gausshyper', 'gamma', 'gengamma', 'genhalflogistic', 'gilbrat', 'gompertz', 'gumbel_r',
                  'gumbel_l', 'halfcauchy', 'halflogistic', 'halfnorm', 'hypsecant', 'invgamma', 'invgauss',
                  'invweibull', 'johnsonsb', 'johnsonsu', 'ksone', 'kstwobign', 'laplace', 'logistic', 'loggamma',
                  'loglaplace', 'lognorm', 'lomax', 'maxwell', 'mielke', 'nakagami', 'ncx2', 'ncf', 'nct', 'norm',
                  'pareto', 'pearson3', 'powerlaw', 'powerlognorm', 'powernorm', 'rdist', 'reciprocal', 'rayleigh',
                  'rice', 'recipinvgauss', 'semicircular', 't', 'triang', 'truncexpon', 'truncnorm', 'tukeylambda',
                  'uniform', 'vonmises', 'wald', 'weibull_min', 'weibull_max', 'wrapcauchy']
    dist_results = []
    params = {}

    for dist_name in dist_names:
        dist = getattr(st, dist_name)
        param = dist.fit(data)
        params[dist_name] = param
        D, p = st.kstest(data, dist_name, args=param)
        dist_results.append((dist_name, p))

    best_dist= (max(dist_results, key=lambda item: item[1]))
    plt.hist(data)
    plt.show()
    print("Best fitting distribution: "+str(best_dist))

get_best_distribution(df['A-G'])
"""