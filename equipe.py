import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import curso as curso
import os.path
import pickle

class Equipe:

    def __init__(self, curso, estudantes):
        self.__curso = curso
        self.__estudantes = estudantes
    

    @property
    def curso(self):
        return self.__curso

    @property
    def estudantes(self):
        return self.__estudantes

class LimiteCriaEquipe(tk.Toplevel):
  def __init__(self, controle, listaCurso, listaEstudante):
      tk.Toplevel.__init__(self)
      self.geometry('300x150')
      self.title("Criação de Equipes")
      self.controle = controle

      self.frameCurso = tk.Frame(self)
      self.frameNumMat = tk.Frame(self)
      self.frameButton = tk.Frame(self)
      self.frameCurso.pack()
      self.frameNumMat.pack()
      self.frameButton.pack()
      

      self.labelCurso = tk.Label(self.frameCurso,text="Escolha o curso: ")
      self.labelCurso.pack(side="left")
      self.escolhaCombo = tk.StringVar()
      self.combobox = ttk.Combobox(self.frameCurso, width = 22 , textvariable = self.escolhaCombo)
      self.combobox.pack(side="left")
      self.combobox['values'] = listaCurso

      self.labelNumMat = tk.Label(self.frameNumMat,text="Informe o número de matrícula: ")
      self.labelNumMat.pack(side="left")
      self.inputNumMat = tk.Entry(self.frameNumMat, width=15)
      self.inputNumMat.pack(side="left")

      self.buttonSubmit = tk.Button(self.frameButton, text="Adicionar estudante")    
      self.buttonSubmit.pack(side="left")
      self.buttonSubmit.bind("<Button>", controle.adicionaEstudante)

      self.buttonSubmit = tk.Button(self.frameButton, text="Criar Equipe")    
      self.buttonSubmit.pack(side="left")
      self.buttonSubmit.bind("<Button>", controle.equipeCriada)


  def mostraJanela(self, titulo, msg):
      messagebox.showinfo(titulo, msg)

class LimiteConsultaEquipe(tk.Toplevel):
  def __init__(self, controle):
      tk.Toplevel.__init__(self)
      self.geometry('300x150')
      self.title("Consultar Equipes")
      self.controle = controle

      self.frameSigla = tk.Frame(self)
      self.frameSigla.pack()
      self.frameButton = tk.Frame(self)
      self.frameButton.pack()

      self.labelSigla = tk.Label(self.frameSigla,text="Informe a sigla do Curso: ")
      self.labelSigla.pack(side="left")
      self.inputSigla = tk.Entry(self.frameSigla, width=15)
      self.inputSigla.pack(side="left")

      self.buttonSubmit = tk.Button(self.frameButton, text="Consultar")
      self.buttonSubmit.pack(side="left")
      self.buttonSubmit.bind("<Button>", controle.consultaEquipe)

  def mostraJanela(self, titulo, msg):
      messagebox.showinfo(titulo, msg)

class InterfaceEstatisticas:
    def __init__(self, root, numero_equipes, numero_estudantes, media_por_equipe):
        self.root = root
        self.root.title("Estatísticas do Campeonato")

        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=20, pady=20)

        self.labelEquipes = tk.Label(self.frame, text=f"Número de equipes: {numero_equipes}")
        self.labelEquipes.pack()

        self.labelEstudantes = tk.Label(self.frame, text=f"Número total de estudantes: {numero_estudantes}")
        self.labelEstudantes.pack()

        self.labelMedia = tk.Label(self.frame, text=f"Média de estudante por equipe: {media_por_equipe:.2f}")
        self.labelMedia.pack()
       

class CtrlEquipe():
  def __init__(self, controlePrincipal):
    self.ctrlPrincipal = controlePrincipal
    self.listaCurso = []
    self.listaEstudante = []

    self.listaEstEquipe = []
    if not os.path.isfile("equipe.pickle"):
      self.listaEquipe = []
    else:
       with open("equipe.pickle", "rb") as f:
          self.listaEquipe = pickle.load(f)

  def salvaEquipe(self):
    if len(self.listaEquipe) != 0:
      with open("equipe.pickle","wb") as f:
        pickle.dump(self.listaEquipe, f)

  def criarEquipe(self):
    self.listaCurso = self.ctrlPrincipal.ctrlCurso.getListaCurso()
    self.listaEstudante = self.ctrlPrincipal.ctrlCurso.getListaEstudante()
    self.limiteCria = LimiteCriaEquipe(self, self.listaCurso, self.listaEstudante)

  def adicionaEstudante(self, event):
    listaEstudantes = self.ctrlPrincipal.ctrlCurso.getListaEstudante()
    Curso = self.limiteCria.escolhaCombo.get()
    Num = int(self.limiteCria.inputNumMat.get())
    chec = 0
    

    for estudante in listaEstudantes:
      if estudante.nroMatric == Num:
        if estudante.curso.nome == Curso:
          self.listaEstEquipe.append(estudante)
          self.limiteCria.mostraJanela("Sucesso", "Estudante selecionado")
          chec = 1

    if chec == 0:
      self.limiteCria.mostraJanela("Erro", "Estudante não encontrado")

  def equipeCriada(self, event):
     Curso = self.limiteCria.escolhaCombo.get()
     Curso2 = self.ctrlPrincipal.ctrlCurso.getCurso(Curso)
     equipe = Equipe(Curso2, self.listaEstEquipe)
     self.listaEquipe.append(equipe)
     self.limiteCria.mostraJanela('Sucesso', 'Equipe criada com sucesso')
     self.limiteCria.destroy()
     self.listaEstEquipe = []

  
  def consultaCurso(self):
     self.limiteConsulta = LimiteConsultaEquipe(self)
  
  def consultaEquipe(self, event):
    sigla = self.limiteConsulta.inputSigla.get()
    listaCurso = self.ctrlPrincipal.ctrlCurso.getListaCurso2()

    chec = 0
    for crs in listaCurso:
        if sigla == crs.sigla:
            chec = 1
            break
    
    if chec == 0:
        self.limiteConsulta.mostraJanela("Erro", "Esta sigla de curso não existe")
        return

    equipe_encontrada = None
    
    for equipe in self.listaEquipe:
        if equipe.curso.sigla == sigla:
            equipe_encontrada = equipe
            break

    if equipe_encontrada:
        alunos_equipe = [estudante.nome for estudante in equipe_encontrada.estudantes]
        alunos = "\n".join(alunos_equipe)
        self.limiteConsulta.mostraJanela("Alunos da Equipe", f"Alunos da equipe {sigla}:\n{alunos}")
    else:
        self.limiteConsulta.mostraJanela('Erro', 'Não existe equipe desse curso')


  def dadosCampeonato(self):
      numero_equipes = len(self.listaEquipe)
      numero_estudantes = sum(len(equipe.estudantes) for equipe in self.listaEquipe)
      media_por_equipe = numero_estudantes / numero_equipes if numero_equipes > 0 else 0

      root = tk.Tk()
      interface_estatisticas = InterfaceEstatisticas(root, numero_equipes, numero_estudantes, media_por_equipe)
      root.mainloop()
    


     


     
       
    
        