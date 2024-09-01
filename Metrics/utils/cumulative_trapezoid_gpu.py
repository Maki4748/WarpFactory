import cupy


def cumulative_trapezoid_gpu(y, x=None, dx=1.0, axis=-1, initial=None):
    """
    Cumulatively integrate y(x) using the composite trapezoidal rule.

    Parameters
    ----------
    y : array_like
        Values to integrate.
    x : array_like, optional
        The coordinate to integrate along. If None (default), use spacing `dx`
        between consecutive elements in `y`.
    dx : float, optional
        Spacing between elements of `y`. Only used if `x` is None.
    axis : int, optional
        Specifies the axis to cumulate. Default is -1 (last axis).
    initial : scalar, optional
        If given, insert this value at the beginning of the returned result.
        0 or None are the only values accepted. Default is None, which means
        `res` has one element less than `y` along the axis of integration.

    Returns
    -------
    res : ndarray
        The result of cumulative integration of `y` along `axis`.
        If `initial` is None, the shape is such that the axis of integration
        has one less value than `y`. If `initial` is given, the shape is equal
        to that of `y`.

    See Also
    --------
    cupy.cumsum, cupy.cumprod
    cumulative_simpson : cumulative integration using Simpson's 1/3 rule
    quad : adaptive quadrature using QUADPACK
    fixed_quad : fixed-order Gaussian quadrature
    dblquad : double integrals
    tplquad : triple integrals
    romb : integrators for sampled data

    Examples
    --------
    >>> from cupyx.scipy import integrate
    >>> import cupy
    >>> import matplotlib.pyplot as plt

    >>> x = cupy.linspace(-2, 2, num=20)
    >>> y = x
    >>> y_int = integrate.cumulative_trapezoid(y, x, initial=0)
    >>> plt.plot(x, y_int, 'ro', x, y[0] + 0.5 * x**2, 'b-')
    >>> plt.show()

    """
    y = cupy.asarray(y)
    if y.shape[axis] == 0:
        raise ValueError("At least one point is required along `axis`.")
    if x is None:
        d = dx
    else:
        x = cupy.asarray(x)
        if x.ndim == 1:
            d = cupy.diff(x)
            # reshape to correct shape
            shape = [1] * y.ndim
            shape[axis] = -1
            d = d.reshape(shape)
        elif len(x.shape) != len(y.shape):
            raise ValueError("If given, shape of x must be 1-D or the "
                             "same as y.")
        else:
            d = cupy.diff(x, axis=axis)

        if d.shape[axis] != y.shape[axis] - 1:
            raise ValueError("If given, length of x along axis must be the "
                             "same as y.")

    nd = len(y.shape)
    slice1 = tupleset((slice(None),)*nd, axis, slice(1, None))
    slice2 = tupleset((slice(None),)*nd, axis, slice(None, -1))
    res = cupy.cumsum(d * (y[slice1] + y[slice2]) / 2.0, axis=axis)

    if initial is not None:
        if initial != 0:
            raise ValueError("`initial` must be `None` or `0`.")
        if not cupy.isscalar(initial):
            raise ValueError("`initial` parameter should be a scalar.")

        shape = list(res.shape)
        shape[axis] = 1
        res = cupy.concatenate([cupy.full(shape, initial, dtype=res.dtype), res],
                             axis=axis)

    return res

def tupleset(t, i, value):
    l = list(t)
    l[i] = value
    return tuple(l)