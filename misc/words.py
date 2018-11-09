from talon.voice import Context, Key, Str

ctx = Context('words')

# This is for remapping certain words to others
# Check out vocab.py for adding and removing vocab
keymap = {

    'batch of facts': 'batch effects',

    'D-plier': 'dplyr',

    'fee': 'phi',

    'Mark': 'mock', 
    
    # from voicecode
    'cove': 'cov',
    'coves': 'covs',
    'a beeline': 'abline',
    'mf row': 'mfrow',
    'lynn': 'lin',
    'ling': 'lin',
    'seek': 'seq',
    'aargh': 'arg',
    'f': 'eff',
    'epps': 'eps',
    'dlf': 'dof',
    'see bond': 'cbind',
    'see bind': 'cbind',
    'freak': 'freq',
    'coif': 'coef',
    'Brian': 'Bryan',
    'brian': 'bryan',
    'john page': 'John Paige',
    'johnny page': 'Johnny Paige',
    'tech': 'tex',
    'csc': 'csz',
    'serum': 'theorem',
    'my turn': 'matern',
    'ge': 'GEE',
    'ge edge': 'GEE',
    'right up': 'writeup',
    'argument x': 'argmax',
    'tex shop': 'texshop',
    'tech shop': 'texshop',
    'dissed': 'dist',
    'org sub': 'argsup',
    'argus up': 'argsup',
    'you dub': 'UW',
    'uw': 'UW',
    'youdub': 'UW',
    'm kl': 'mkl',
    'ea z': 'EAs',
    'bays': 'Bayes',
    'climber': '!',
    'bailey of seismic': 'paleoseismic',
    'paley of seismic': 'paleoseismic',
    'balliol seismic': 'paleoseismic',
    'atom': 'Adam',
    'spiro': 'Szpiro',
    'Atom Szpiro': 'Adam Szpiro',
    'Goot Torp': 'Guttorp',
    'Do Torp': 'Guttorp',
    'dear ashley': 'dirichlet',
    'Week field': 'Wakefield',
    'Weak field': 'Wakefield',
    'Wake field': 'Wakefield',
    'waitsfield': 'Wakefield',
    'john wakefield': 'Jon Wakefield',
    'jaunt': 'Jon',
    'Nisha': 'Nychka',
    'noah': 'NOAA',
    'corm': 'QERM',
    'gsr': 'GSR',
    'jono': 'jonno',
    'ta': 'TA',
    'ra': 'RA',
    'latticekrig': 'latticeKrig',
    'urban a city': 'urbanicity',
    'e-mail': 'email',
    'phd': 'PhD',
    'mishka': 'Nychka',
    'albin': 'Albyn',
    'alvin': 'Albyn',
    'albion': 'Albyn',
    'paigejo @ gmail.com': 'paigejo@gmail.com',
    'paigejo at UW.edu': 'paigejo@uw.edu',
    'plus on': 'Poisson',
    'Joni': 'Johnny',
    'trace back': 'traceback',
    'numb': 'num',
    'ro': 'row',
    'limb': 'lim',
    'limbs': 'lims',
    'frak': 'frac',
    'lujan': 'logit',
    'ids': 'IDs',
    'latin': 'lat',
    'estes': 'sds',
    'her cold far': 'HHoldVar',
    'all right': 'alright',
    'quintile': 'quantile',
    '1 tile': 'quantile',
    'quan tile': 'quantile',
    'Joni': 'Johnny',
    'I hme': 'IHME',
    'float barrier': 'FloatBarrier',
    'geyer are not': 'Geir-Arne',
    'geyer anna': 'Geir-Arne',
    'aerial': 'areal',
    'I car': 'ICAR',
    'din': 'dim',
    'rose': 'rows',
    'tracks': 'x',
    'mech': 'mesh',
    'nully': 'null',
    'c dot': 'cdot',
    'logger': 'log',
    'lug are': 'log',
    'blogger': 'log',
    'jen': 'gen',
    'rez': 'res',
    'erin': 'Aaron',
    'hume sum': 'cumsum',
    'hume some': 'cumsum',
    'kim sum': 'cumsum',
    'kim some': 'cumsum',
    'humanism': 'cumsum',
    'champ attracts': 'X',
    'Attracts': 'X',
    'on list': 'unlist',
    'bassist': 'basis',
    'be splines': 'b splines',
    'be spline': 'b spline',
    'identify ability': 'identifiability',
    'identified ability': 'identifiability',
    'creaking': 'kriging',
    'probe it': 'probit',
    'fix defects': 'fixed effects',
    'quan tile': 'quantile',
    'parens': 'params',
    'param s': 'params',
    'param z': 'params',
    'chord': 'coord',
    'chords': 'coords',
    'sins': 'sims',
    'temp oral': 'temporal',
    'psalms': 'sums',
    'lawtex': 'latex',
    'mk dear': 'mkdir',
    'no him': 'num',
    'msc': 'mse',
    'twd': 'pwd',
    'two': 'to',
    'mouse': 'm',
    'mouth': 'm',
    'one': 'one',
    'jan': 'gen',
    'emily': 'MLE',
    'exchange ability': 'exchangeability',
    'halcyon': 'hessian',
}

ctx.keymap(keymap)