
def dobro(a=None):
	if is_number(a):
		return float(a)*2
	else:
		return None

def half(b=None):
	if is_number(b):
		return float(b)/2
	else:
		return None

def is_number(x):
	try:
		float(x)
		return True
	except ValueError:
		return False

def soma(s=None, d=None):
	if is_number(s) and is_number(d):
		return float(s) + float(d)
	else:
		return None

def subtracao(q=None, w=None):
	if is_number(q) and is_number(w):
		return float(q) - float(w)
	else:
		return None

def mult(z, c):
	if is_number(z) and is_number(c):
		return float(z) * float(c)
	else:
		return None
