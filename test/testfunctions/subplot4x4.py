# -*- coding: utf-8 -*-
#
desc = '$4\\times 4$ subplots'
# phash = 'a19c3f529adc3313'
phash = 'eb9c3f129edc0303'


def plot():
    from matplotlib import pyplot as pp
    import numpy as np

    fig = pp.figure()

    an = np.linspace(0, 2*np.pi, 100)

    pp.subplot(221)
    pp.plot(3*np.cos(an), 3*np.sin(an))
    pp.title('not equal, looks like ellipse', fontsize=10)

    pp.subplot(222)
    pp.plot(3*np.cos(an), 3*np.sin(an))
    pp.axis('equal')
    pp.title('equal, looks like circle', fontsize=10)

    pp.subplot(223)
    pp.plot(3*np.cos(an), 3*np.sin(an))
    pp.axis('equal')
    pp.axis([-3, 3, -3, 3])
    pp.title('looks like circle, even after changing limits', fontsize=10)

    pp.subplot(224)
    pp.plot(3*np.cos(an), 3*np.sin(an))
    pp.axis('equal')
    pp.axis([-3, 3, -3, 3])
    pp.plot([0, 4], [0, 4])
    pp.title('still equal after adding line', fontsize=10)

    return fig
