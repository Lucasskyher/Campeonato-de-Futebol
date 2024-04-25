import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


class Curso:
  def __init__(self, sigla, nome):
    self.__sigla = sigla
    self.__nome = nome

  @property
  def sigla(self):
    return self.__sigla

  @property
  def nome(self):
    return self.__nome

class Estudante:
  def __init__(self, nroMatric, nome, curso):
    self.__nroMatric = nroMatric
    self.__nome = nome
    self.__curso = curso

  @property
  def nroMatric(self):
    return self.__nroMatric

  @property
  def nome(self):
    return self.__nome

  @property
  def curso(self):
    return self.__curso

class CtrlCurso():
  def __init__(self):
    self.listaCurso = []
    self.listaEstudante = []
    c1 = Curso("CCO", "Ciência da Computação")
    c2 = Curso("SIN", "Sistemas de Informação")
    c3 = Curso("EEL", "Engenharia Elétrica")
    self.listaCurso.append(c1)
    self.listaCurso.append(c2)
    self.listaCurso.append(c3)
    self.listaEstudante.append(Estudante(1001, "José da Silva", c1))
    self.listaEstudante.append(Estudante(1002, "João de Souza", c1))
    self.listaEstudante.append(Estudante(1003, "Rui Santos", c2))
    self.listaEstudante.append(Estudante(1004, "Maria Oliveira", c2))
    self.listaEstudante.append(Estudante(1005, "Pedro Henrique", c2))
    self.listaEstudante.append(Estudante(1006, "Ana Luiza", c3))
    self.listaEstudante.append(Estudante(1007, "Mariana Silva", c3))
    self.listaEstudante.append(Estudante(1008, "Paulo Roberto", c1))
    self.listaEstudante.append(Estudante(1009, "Fernanda Santos", c1))
    self.listaEstudante.append(Estudante(1010, "Lucas Souza", c3))
    
  def getListaCurso(self):
    listaNome = []
    for crs in self.listaCurso:
      listaNome.append(crs.nome)
    return listaNome  

  def getListaEstudante(self):
    return self.listaEstudante
  
  def getListaCurso2(self):
    return self.listaCurso
  
  def getListaEstudanteCurso(self):
    listaEstudanteCurso = []
    for est in self.listaEstudante:
      listaEstudanteCurso.append(est.curso)
    return listaEstudanteCurso
  
  def getCurso(self, CursoNome):
    cursoRet = None
    for crs in self.listaCurso:
      if crs.nome == CursoNome:
        cursoRet = crs
    return cursoRet
      


class CtrlEstudante():
  def __init__(self):
    self.listaEstudante = []
  

  def getListaEstudante(self):
    return self.listaEstudante
          
      
