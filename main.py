import tkinter as tk
from tkinter import messagebox
import curso as crs
import equipe as eq


class LimitePrincipal():
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry('350x200')
        self.menubar = tk.Menu(self.root)        
        self.criarMenu = tk.Menu(self.menubar)
        self.consultarMenu = tk.Menu(self.menubar)
        self.imprimirMenu = tk.Menu(self.menubar)
        self.sairMenu = tk.Menu(self.menubar)

        self.criarMenu.add_command(label="Criar equipe", \
                    command=self.controle.criarEquipe)
        self.menubar.add_cascade(label="Criar", \
                    menu=self.criarMenu)

        self.consultarMenu.add_command(label="Consultar equipe", \
                    command=self.controle.consultaCurso)
        self.menubar.add_cascade(label="Consultar", \
                    menu=self.consultarMenu)

        self.imprimirMenu.add_command(label="Imprimir dados", \
                    command=self.controle.dadosCampeonato)
        self.menubar.add_cascade(label="Imprimir", \
                    menu=self.imprimirMenu)

        self.root.config(menu=self.menubar)

class ControlePrincipal():       
  def __init__(self):
      self.root = tk.Tk()

      self.ctrlCurso = crs.CtrlCurso()
      self.ctrlEquipe = eq.CtrlEquipe(self)
      self.ctrlEstudante = crs.CtrlEstudante()

      self.limite = LimitePrincipal(self.root, self) 

      self.root.title("Campeonato de Futebol")
      # Inicia o mainloop
      self.root.mainloop()

      self.ctrlEquipe.salvaEquipe()
        
  def criarEquipe(self):
      self.ctrlEquipe.criarEquipe()

  def consultaCurso(self):
      self.ctrlEquipe.consultaCurso()

  def dadosCampeonato(self):
      self.ctrlEquipe.dadosCampeonato()
    

if __name__ == '__main__':
  c = ControlePrincipal()