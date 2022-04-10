
from datetime import datetime
import random
from flask import Flask, jsonify, request
import json

class Book:
    Data = []
    contador = 0

    def New_Book(self, busqueda, Autor, Titulo, Edicion, Year, Copias,Bookshelf, Bookshelf_row):
        try:
            
            for j in range(len(self.Data)):
                if self.Data[j][0] == busqueda:                    
                    return jsonify({"msg": "ISBN Dublicado"}),400

            self.Data.append([])

            for i in range(9):
                self.Data[self.contador].append("")
            self.Data[self.contador][0] = busqueda
            self.Data[self.contador][1] = Autor
            self.Data[self.contador][2] = Titulo
            self.Data[self.contador][3] = Edicion
            self.Data[self.contador][4] = int(Year)
            self.Data[self.contador][5] = int(Copias)
            self.Data[self.contador][6] = self.Data[self.contador][5]
            self.Data[self.contador][7] = Bookshelf
            self.Data[self.contador][8] = Bookshelf_row
            self.contador += 1
            return jsonify({"msg": "Libro Creado Exitosamente"})
        except ValueError:
            return jsonify({"msg":"Ingrese numeros no caracteres en Year o Copias"}), 400
    
    def Edit_Information(self,ISBN, Autor, Titulo, Edicion, Year, Copias,Bookshelf, Bookshelf_row):
            
        for i in range(len(self.Data)):
            if ISBN == self.Data[i][0]:
                
                self.Data[i][1] = Autor
                self.Data[i][2] = Titulo
                self.Data[i][3] = Edicion
                self.Data[i][4] = int(Year)
                self.Data[i][6] += int(Copias)
                if self.Data[i][6] < 0:
                    self.Data[i][6] = 0
                self.Data[i][7] = Bookshelf
                self.Data[i][8] = Bookshelf_row
                return jsonify({"msg": "Cambios Guardados Exitosamente"})
        return jsonify({"msg": "Ese ISBN no existe en el Sistema"}),404    
                    
    def Search_Book_Filter(self,Titulo,De,A,Autor):
        Total = []
        if De and A == " " and Autor == " " and Titulo == " ":
            for i in range(len(self.Data)):
                search = {
                "ISBN": self.Data[i][0],
                "Autor": self.Data[i][1],
                "Titulo": self.Data[i][2],
                "Year": self.Data[i][4],
                "Copias": self.Data[i][5],
                "Copias_Disponibles": self.Data[i][6]
                }
                Total.append(search)
            return json.dumps(Total,indent=4)
        if De and A != "" and Autor == " " and Titulo == " ":
            for i in range(len(self.Data)):
                if int(De)<=self.Data[i][4]<=int(A):
                    search = {
                    "ISBN": self.Data[i][0],
                    "Autor": self.Data[i][1],
                    "Titulo": self.Data[i][2],
                    "Year": self.Data[i][4],
                    "Copias": self.Data[i][5],
                    "Copias_Disponibles": self.Data[i][6]
                    }
                    Total.append(search)
            return  json.dumps(Total,indent=4)
        if De and A == " " and Autor != "" and Titulo == " ":
            for i in range(len(self.Data)):
                if self.Data[i][1] == Autor:
                    search = {
                    "ISBN": self.Data[i][0],
                    "Autor": self.Data[i][1],
                    "Titulo": self.Data[i][2],
                    "Year": self.Data[i][4],
                    "Copias": self.Data[i][5],
                    "Copias_Disponibles": self.Data[i][6]
                    }
                    Total.append(search)
            return  json.dumps(Total,indent=4)
        if De and A != "" and Autor != "" and Titulo != "":
            for i in range(len(self.Data)):
                if int(De)<=self.Data[i][4]<=int(A) and self.Data[i][1] == Autor and self.Data[i][2] == Titulo:
                    search = {
                    "ISBN": self.Data[i][0],
                    "Autor": self.Data[i][1],
                    "Titulo": self.Data[i][2],
                    "Year": self.Data[i][4],
                    "Copias": self.Data[i][5],
                    "Copias_Disponibles": self.Data[i][6]
                    }
                    Total.append(search)
            return Total
        if De and A == " " and Autor == " " and Titulo != "":
            for i in range(len(self.Data)):
                if self.Data[i][1] == Autor:
                    search = {
                    "ISBN": self.Data[i][0],
                    "Autor": self.Data[i][1],
                    "Titulo": self.Data[i][2],
                    "Year": self.Data[i][4],
                    "Copias": self.Data[i][5],
                    "Copias_Disponibles": self.Data[i][6]
                    }
                    Total.append(search)
            return  json.dumps(Total,indent=4)    
                                
class Lender:
    Data_lender = []
    contador = 0
    
    def New_lender(self,CUI,Nombre,Apellido):
        for j in range(len(self.Data_lender)):
            if self.Data_lender[j][0] == CUI:
                return jsonify({"msg": "CUI Duplicado"}),400
        self.Data_lender.append([])
        for i in range(6):
            self.Data_lender[self.contador].append("")
        self.Data_lender[self.contador][0] = CUI
        self.Data_lender[self.contador][1] = Nombre
        self.Data_lender[self.contador][2] = Apellido
        self.Data_lender[self.contador][3] = 1
        self.Data_lender[self.contador][4] = ""
        self.Data_lender[self.contador][5] = 6
        self.contador += 1
        return jsonify({"msg": "Prestamista Creado Exitosamente"})
    
    def Lend_Book(self,CUI,ISBN):
        for i in range(len(self.Data_lender)):
            if self.Data_lender[i][0] == CUI:
                if self.Data_lender[i][3] == 0:
                    return jsonify({"msg":"ya ah prestado un libro devuelva el libro prestado"}), 400
                for j in range(len(book.Data)):
                    if book.Data[j][0] == ISBN:
                        self.Data_lender[i].append([])
                        for k in range(5):
                            self.Data_lender[i][self.Data_lender[i][5]].append("")
                        uuid = random.randint(10000,99999)
                        self.Data_lender[i][self.Data_lender[i][5]][0] = uuid
                        self.Data_lender[i][4] = uuid
                        self.Data_lender[i][self.Data_lender[i][5]][1] = book.Data[j][0]
                        self.Data_lender[i][self.Data_lender[i][5]][2] = book.Data[j][2]
                        self.Data_lender[i][self.Data_lender[i][5]][3] = datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
                        self.Data_lender[i][self.Data_lender[i][5]][4] = "--/--/--"
                        self.Data_lender[i][5] += 1
                        book.Data[j][6] -= 1
                        self.Data_lender[i][3] -= 1    
                        return jsonify({"msg":"Prestamo hecho exitosamente>>> UUID:{}".format(uuid)})
                return jsonify({"msg":"El ISBN no existe en el Sistema"}),404
        return jsonify({"msg":"El CUI no existe en el Sistema"}),404
    
    def Return_Book(self,uuid):
        uuid2 = int(uuid)
        for i in range(len(self.Data_lender)):
            if self.Data_lender[i][4] == uuid2:
                for j in range(len(book.Data)):
                    if book.Data[j][0] == self.Data_lender[i][self.Data_lender[i][5]-1][1]:
                        book.Data[j][6] += 1
                self.Data_lender[i][self.Data_lender[i][5]-1][4] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                
                self.Data_lender[i][3] += 1
                
                
                return jsonify({"msg":"Devolucion hecha exitosamente"})
        return jsonify({"msg":"No existe ese UUID en nuestra base de datos"}),404   
    
    def Search_Lender(self,CUI):
        total = []
        
        for i in range(len(self.Data_lender)):
            if self.Data_lender[i][0] == CUI:
                if self.Data_lender[i][5] != 6:
                    for j in range(5,self.Data_lender[i][5]):
                        if 6<=j<=100:
                            historial = {
                            "UUID":self.Data_lender[i][j][0]
                            ,"ISBN":self.Data_lender[i][j][1]
                            ,"Titulo":self.Data_lender[i][j][2]
                            ,"Fecha_Prestamo":self.Data_lender[i][j][3],
                            "Fecha_Devolucion":self.Data_lender[i][j][4],
                            }    
                            total.append(historial)
                
                peticion = {
                    "CUI": self.Data_lender[i][0],
                    "Nombre":self.Data_lender[i][1],
                    "Apellido":self.Data_lender[i][2],
                    "Historial de Prestamos":total
                    

                }
                return json.dumps(peticion,indent=4)
                
        return jsonify({"msg":"El CUI no existe en el Sistema"}),404     
  
book = Book()
lender = Lender()
app = Flask(__name__) 
if __name__ == "__main__":
    app.run(debug = True)
##======================Libros RUTAS=========================


@app.route('/Book_Filter', methods = ["GET"])
def GET_Search_Book_Filter():
    peticion={
        "Titulo" : request.json["Titulo"],
        "De": request.json["De"],
        "A": request.json["A"],
        "Autor": request.json["Autor"]
    }        
    return book.Search_Book_Filter(peticion.get("Titulo"),peticion.get("De"),peticion.get("A"),peticion.get("Autor"))

@app.route('/New_Book', methods = ["POST"] )
def POST_New_Book():
    
    peticion = {
        "ISBN": request.json["ISBN"],
        "Autor": request.json["Autor"],
        "Titulo": request.json["Titulo"],
        "Edicion": request.json["Edicion"],
        "Year": request.json["Year"],
        "Copias": request.json["Copias"],
        "Bookshelf": request.json["Bookshelf"],
        "Bookshelf_row": request.json["Bookshelf_row"]
        
        
    }
    
    
    return book.New_Book(peticion.get("ISBN"),peticion.get("Autor"),peticion.get("Titulo"),peticion.get("Edicion"),peticion.get("Year"),peticion.get("Copias"),peticion.get("Bookshelf"),peticion.get("Bookshelf_row"))

@app.route('/Edit_Book', methods = ["PUT"])
def PUT_Edit_Information():
    peticion = {
        "ISBN": request.json["ISBN"],
        "Autor": request.json["Autor"],
        "Titulo": request.json["Titulo"],
        "Edicion": request.json["Edicion"],
        "Year": request.json["Year"],
        "Copias_Agregar": request.json["Copias_Agregar"],
        "Bookshelf": request.json["Bookshelf"],
        "Bookshelf_row": request.json["Bookshelf_row"]     
    }
    try:
        Year = int(peticion.get("Year"))
        Copias_Agregar = int(peticion.get("Copias_Agregar"))
    except ValueError:
        return jsonify({"msg":"Colocar Numeros no caracteres en Year y Copias A agregar"}),400
    return book.Edit_Information(peticion.get("ISBN"),peticion.get("Autor"),peticion.get("Titulo"),peticion.get("Edicion"),Year,Copias_Agregar,peticion.get("Bookshelf"),peticion.get("Bookshelf_row"))
##===================Prestamistas Rutas===================================    
@app.route('/New_Lender', methods = ["POST"] )
def POST_New_Lender():
    
    peticion = {
        "CUI": request.json["CUI"],
        "Nombre": request.json["Nombre"],
        "Apellido": request.json["Apellido"], 
    } 
    return lender.New_lender(peticion.get("CUI"),peticion.get("Nombre"),peticion.get("Apellido")) 

@app.route('/Lend_Book', methods = ["POST"])
def POST_Lend_Book():
    peticion = {
        "CUI": request.json["CUI"],
        "ISBN": request.json["ISBN"]
    }
    return lender.Lend_Book(peticion.get("CUI"),peticion.get("ISBN"))

@app.route('/Return_Book', methods = ["PATCH"])
def PATCH_Return_Book():
    peticion = {
        "UUID" : request.json["UUID"]
    }
    return lender.Return_Book(peticion.get("UUID"))

@app.route('/Search_Lender', methods = ["GET"] )
def GET_Search_Lender():
    peticion = {
        "CUI": request.json["CUI"]
    } 
    return lender.Search_Lender(peticion.get("CUI"))     
                        