var1 = b'\x35\x02\x63\x0E\x19\x3D\x1F\x03\x1C\x06\x50\x0E\x49\x1D\x08\x4C\x05\x0D\x3C\x32\x19\x2C\x0B\x0B\x29\x67\x24'
var2 = b'AjR}(N+p}26=9)=yr=NVzD8hBTV\%c'

def xor_everything(n1, n2):
	return bytes([b ^ k for b, k in zip(n1, n2)])
print(xor_everything(var1, var2))