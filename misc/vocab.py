from talon.voice import Context

# I'm using this to replace my use of words.py
ctx = Context('vocab_amy')

ctx.vocab = [
    # important to keep this in alphabetical order! Here's some R code to print and sort words:
    # sortedWords = sort(allWords)
    # test = paste0("'", paste(sortedWords, collapse="', '"), "'")
    # 'batch effects',
    # 'bal',
    # 'Bayes',
    # 'biostatistics',
    # 'Bryan',
    # 
    # 'CAGs',
    # 'Cholesky',
    # 'cor',
    # 'corncob',
    # 'cov',
    # 
    # 'dat',
    # 'deg',
    # 'dev',
    # 'dist',
    # 'dists',
    # 
    # 'est',
    # 'exp',
    # 'expit',
    # 
    # 'fin',
    # 'Frequentist',
    # 
    # 'gen',
    # 'gene',
    # 'genome',
    # 'genomes',
    # 'genus',
    # 
    # 'ind',
    # 'inla',
    # 
    # 'kriging', 
    # 
    # 'lat',
    # 'LatticeKrig',
    # 'len',
    # 'lim',
    # 'logit',
    # 'lon',
    # 'Lostreia',
    # 'Lostreian',
    # 
    # 'mat',
    # 'metagenome',
    # 'metagenomic',
    # 'metagenomics',
    # 'mfrow',
    # 'mock', 
    # 'modeling',
    # 'mort',
    # 'MSE',
    # 
    # 'ncol',
    # 'nonparametric',
    # 'nrow',
    # 
    # 'Okada', 
    # 'OTU',
    # 
    # 'p-value',
    # 'p-values',
    # 'parameterizations',
    # 'pred',
    # 'preds',
    # 'psd',
    # 
    # 'reparameterization',
    # 'res',
    # 'resids',
    # 'rev',
    # 
    # 'seq',
    # 'semiparametric',
    # 'SRS',
    # 
    # 'talon',
    # 'taxa',
    # 'taxon',
    # 'tibble',
    # 
    # 'val',
    # 'vec',
    # 
    # 
    # 
    # 
    # 
    # 'reg',
    # 'surv',
    # 'hist',
    # 'num',
    # 'freq',
    # 'prob',
    # 'probs',
    # 'dens',
    # 'geo',
    # 'sub',
    # 'subs',
    # 'XLab',
    # 'YLab',
    # 'XLim',
    # 'YLim',
    # 'ZLim',
    # 'CLim',
    # 'CEX',
    # 'clust',
    # 'ang',
    # 'BYM',
    # 'XTable',
    # 'SD',
    # 'SDs',
    # 'SE',
    # 'SEs',
    # 'distn',
    # 'WD',
    # 'TMP',
    # 'col',
    # 'res',
    # 'interp',
    # 'fac',
    # 'GGPlot',
    # 'RGDal',
    # 'SP',
    # 'util',
    # 'CRPS',
    # 'ABLine',
    # 'samp',
    # 'proj',
    # 'val',
    # 'vals',
    # 'SApply',
    # 'MApply',
    # 'LApply',
    # 'inv',
    # 'PTS',
    # 'strat',
    # 'strata',
    # 'urb',
    # 'CRS',
    # 'ATTR',
    # 'UTM',
    # 'dir',
    # 'LKInla',
    # 'LK',
    # 'eff',
    # 'DOF',
    # 'SQ',
    # 'init',
    # 'par',
    # 'obs',
    # 'coef',
    # 'coefs',
    # 'marg',
    # 'lin',
    # 'quant',
    # 'comp',
    # 'med',
    # 'CMD',
    # 'arg',
    # 'args',
    # 'unif',
    # 'sim',
    # 'sims',
    # 'LTY',
    # 'hyperpar',
    # 'hyperpars',
    # 'hyperparameter',
    # 'hyperparameters',
    # 'CBind',
    # 'RBind',
    # 'int',
    # 'inf',
    # 'eps',
    # 'CI',
    # 'EA',
    # "argmin",
    # "argmax",
    # "argsup",
    # "arginf",
    # "sup",
    # "cdot",
    # "nabla",
    # "varphi",
    # "RM",
    # "paleoseismic",
    # "jonno",
    # "krig",
    # "Guttorp",
    # "Wakefield",
    # "Szpiro",
    # "QERM",
    # "MKL",
    # "RA",
    # "RAs",
    # "TA",
    # "TAs",
    # "NOAA",
    # "krig",
    # "diag",
    # "cont",
    # "undebug",
    # "Nychka",
    # "Farah",
    # "youdub",
    # "IHME",
    # "ICAR",
    # "approx",
    # "asymptotics",
    # "git",
    # "reparameterized",
    # "reparameterize",
    # "mbg",
    # "gbd",
    # "lbd",
    # "quartic",
    # "quintic",
    # "covs",
    # "lims",
    # "interpolator",
    # "prec",
    # "param",
    # "quantile",
    # "sims",
    # "GAM",
    # "TMB",
    # "pwd",
    # "MLE",
    # "latex", 
    # 'paigejo', 
    
    'ABLine', 'ang', 'approx', 'arg', 'arginf', 'argmax', 'argmin', 'args', 'argsup', 
    'asymptotics', 'ATTR', 'bal', 'Bayes', 'biostatistics', 'Bryan', 'BYM', 'CAGs', 
    'CBind', 'cdot', 'CEX', 'Cholesky', 'CI', 'CLim', 'clust', 'CMD', 'coef', 'coefs', 
    'col', 'comp', 'cont', 'cor', 'corncob', 'cov', 'covs', 'CRPS', 'CRS', 'dat', 'deg', 
    'dens', 'dev', 'diag', 'dir', 'dist', 'distn', 'dists', 'DOF', 'EA', 'eff', 'eps', 
    'est', 'exp', 'expit', 'fac', 'Farah', 'fin', 'freq', 'Frequentist', 'GAM', 'gbd', 
    'gen', 'gene', 'genome', 'genomes', 'genus', 'geo', 'GGPlot', 'git', 'Guttorp', 
    'hist', 'hyperpar', 'hyperparameter', 'hyperparameters', 'hyperpars', 'ICAR', 
    'IHME', 'ind', 'inf', 'init', 'inla', 'int', 'interp', 'interpolator', 'inv', 'jitter', 'jittered', 
    'jonno', 'krig', 'krig', 'kriging', 'LApply', 'lat', 'latex', 'LatticeKrig', 'lbd', 
    'len', 'lim', 'lims', 'lin', 'LK', 'LKInla', 'logit', 'lon', 'Lostreia', 'Lostreian', 
    'LTY', 'MApply', 'marg', 'mat', 'mbg', 'med', 'metagenome', 'metagenomic', 
    'metagenomics', 'mfrow', 'MKL', 'MLE', 'mock', 'modeling', 'mort', 'MSE', 'nabla', 
    'ncol', 'NOAA', 'nonparametric', 'nrow', 'num', 'Nychka', 'obs', 'Okada', 'OTU', 
    'p-value', 'p-values', 'paigejo', 'paleoseismic', 'par', 'param', 
    'parameterizations', 'prec', 'pred', 'preds', 'prob', 'probs', 'proj', 'psd', 'PTS', 
    'pwd', 'QERM', 'quant', 'quantile', 'quartic', 'quintic', 'RA', 'RAs', 'RBind', 
    'reg', 'reparameterization', 'reparameterize', 'reparameterized', 'res', 'res', 
    'resids', 'rev', 'RGDal', 'RM', 'samp', 'SApply', 'SD', 'SDs', 'SE', 
    'semiparametric', 'seq', 'SEs', 'sim', 'sims', 'sims', 'SP', 'SQ', 'SRS', 'strat', 
    'strata', 'sub', 'subs', 'sup', 'surv', 'Szpiro', 'TA', 'talon', 'TAs', 'taxa', 
    'taxon', 'tibble', 'TMB', 'TMP', 'undebug', 'unif', 'urb', 'util', 'UTM', 'val', 
    'val', 'vals', 'varphi', 'vec', 'Wakefield', 'WD', 'XLab', 'XLim', 'XTable', 'YLab', 
    'YLim', 'youdub', 'ZLim', 
]

ctx.vocab_remove = [
    'Brian',

    'Daniel',

    'Gino',

    'Jean',

    'modelling',
    
    'lawtex', 

    'P value',
    'P values',

    # 'tax',
    'cuesta', 

]
