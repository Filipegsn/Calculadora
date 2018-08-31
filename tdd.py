import pytest
from app import dobro, half, soma, subtracao, mult

def test_dobro():
	assert dobro(1)==2
	assert dobro(2)==4
	assert dobro(-5)==-10
	assert dobro('1')==2
	assert dobro ('22')== 44
	assert dobro(336.15)==672.30
	assert dobro('Filipe')==None

def test_half():
	assert half(2)==1
	assert half(150)==75
	assert half('10')==5
	assert half('222')==111
	assert half('40.5')==20.25
	assert half(5)==2.5
	assert half(255)==127.5
	assert half('a')==None

def test_soma():
	assert soma(5, 5)== 10
	assert soma(48, 2)==50
	assert soma(-17, 6)==-11
	assert soma(-22, -57)==-79
	assert soma(-63.4, 148.68)==85.28
	assert soma('2', '15')==17
	assert soma('F', 90)==None

def test_subtracao():
	assert subtracao(2, 2)==0
	assert subtracao(-9, 14)==-23
	assert subtracao(2.5, 5)==-2.5
	assert subtracao('12', '7')==5
	assert subtracao('F', 2)==None

def test_mult():
	assert mult(2, 2)==4
	assert mult(-15, 20)==-300
	assert mult('23', '4')==92
	assert mult('d&d', '2')==None
