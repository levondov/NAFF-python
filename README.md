# NAFF for python

Simple implementation of the NAFF algorithm in python [1].

[1] J. Laskar, "Frequency analysis for multi-dimensional systems. Global dynamics and diffusion", Physica D 67, 257281, 1993.


## Example
```python
>>> from naff import *
>>> 
>>> Q = 0.1234
>>> t = np.linspace(0,1000,1001)
>>> X = np.sin(2*np.pi*Q*t)
>>> 
>>> freq,amp = naff(X)
>>> 
>>> freq
[0.12340000001893119]
```


