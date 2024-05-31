from flask import Flask, request, jsonify, json  

app = Flask(__name__)

# Inicializamos un diccionario vacío
diccionario = {}

# 1-.Ruta para obtener el diccionario actual
@app.route('/get_diccionario', methods=['GET'])
def get_diccionario():
    return jsonify(diccionario)

# 2-.Ruta para agregar una clave-valor al diccionario
@app.route('/agregar_clave_valor/<string:clave>/<string:valor>', methods=['GET'])
def agregar_clave_valor_route(clave, valor):
    diccionario[clave] = valor
    return jsonify(diccionario)

# 3-.Ruta para eliminar una clave del diccionario
@app.route('/eliminar_clave/<string:clave>', methods=['GET'])
def eliminar_clave(clave):
    if clave in diccionario:
        del diccionario[clave]
        return jsonify(diccionario)
    else:
        return 'La clave no existe en el diccionario', 404

# 4-.Ruta para modificar el valor de una clave en el diccionario
@app.route('/modificar_valor/<string:clave>/<string:nuevo_valor>', methods=['GET'])
def modificar_valor(clave, nuevo_valor):
    if clave in diccionario:
        diccionario[clave] = nuevo_valor
        return jsonify(diccionario)
    else:
        return 'La clave no existe en el diccionario', 404

# 5-.Ruta para combinar dos diccionarios mediante parámetros de consulta
@app.route('/combinar_diccionarios', methods=['GET'])
def combinar_diccionarios():
    diccionario2_str = request.args.get('diccionario2')
    if not diccionario2_str:
        return 'Parámetro "diccionario2" no proporcionado en la URL', 400

    try:
        diccionario2 = eval(diccionario2_str)
        if not isinstance(diccionario2, dict):
            raise ValueError()
    except (SyntaxError, ValueError):
        return 'El parámetro "diccionario2" no es un diccionario válido', 400

    diccionario.update(diccionario2)
    return jsonify(diccionario)

# 6-.Ruta para agregar un elemento a un conjunto
@app.route('/agregar_elemento_conjunto/<string:elemento>', methods=['GET'])
def agregar_elemento_conjunto(elemento):
    if 'conjunto' not in request.args:
        request.args['conjunto'] = '[]'
    conjunto = set(json.loads(request.args['conjunto']))
    conjunto.add(elemento)
    return jsonify(list(conjunto))

# 7-.Ruta para eliminar un elemento de un conjunto
@app.route('/eliminar_elemento_conjunto/<string:elemento>', methods=['GET'])
def eliminar_elemento_conjunto(elemento):
    if 'conjunto' not in request.args:
        request.args['conjunto'] = '[]'
    conjunto = set(json.loads(request.args['conjunto']))
    if elemento in conjunto:
        conjunto.remove(elemento)
        return jsonify(list(conjunto))
    else:
        return 'El elemento no existe en el conjunto', 404

# 8-.Ruta para combinar dos conjuntos
@app.route('/combinar_conjuntos', methods=['GET'])
def combinar_conjuntos():
    if 'conjunto1' not in request.args:
        request.args['conjunto1'] = '[]'
    if 'conjunto2' not in request.args:
        request.args['conjunto2'] = '[]'
    conjunto1 = set(json.loads(request.args['conjunto1']))
    conjunto2 = set(json.loads(request.args['conjunto2']))
    conjunto_resultante = conjunto1.union(conjunto2)
    return jsonify(list(conjunto_resultante))

# 9-.Ruta para obtener la diferencia entre dos conjuntos
@app.route('/diferencia_entre_conjuntos', methods=['GET'])
def diferencia_entre_conjuntos():
    if 'conjunto1' not in request.args:
        request.args['conjunto1'] = '[]'
    if 'conjunto2' not in request.args:
        request.args['conjunto2'] = '[]'
    conjunto1 = set(json.loads(request.args['conjunto1']))
    conjunto2 = set(json.loads(request.args['conjunto2']))
    diferencia = conjunto1.difference(conjunto2)
    return jsonify(list(diferencia))

# 10-.Ruta para agregar un elemento a una tupla y crear una nueva tupla
@app.route('/agregar_elemento_tupla/<string:elemento>/<tupla>', methods=['GET'])
def agregar_elemento_tupla(elemento, tupla):
    tupla_list = json.loads(tupla)
    tupla_list.append(elemento)
    nueva_tupla = tuple(tupla_list)
    return jsonify(list(nueva_tupla))

# 11-.Ruta para eliminar un elemento de una tupla y crear una nueva tupla
@app.route('/eliminar_elemento_tupla/<string:elemento>', methods=['GET'])
def eliminar_elemento_tupla(elemento):
    if 'tupla' not in request.args:
        return 'La tupla no se proporcionó en la URL', 400

    tupla_str = request.args['tupla']
    tupla = eval(tupla_str)  # Analiza la cadena para obtener la tupla
    nueva_tupla = tuple(e for e in tupla if e != elemento)
    return jsonify(list(nueva_tupla))
# 12-.Ruta para concatenar dos tuplas en una nueva tupla
@app.route('/concatenar_tuplas', methods=['GET'])
def concatenar_tuplas():
    if 'tupla1' not in request.args:
        return 'La tupla1 no se proporcionó en la URL', 400
    if 'tupla2' not in request.args:
        return 'La tupla2 no se proporcionó en la URL', 400

    tupla1_str = request.args['tupla1']
    tupla2_str = request.args['tupla2']

    tupla1 = tuple(json.loads(tupla1_str))
    tupla2 = tuple(json.loads(tupla2_str))

    nueva_tupla = tupla1 + tupla2
    return jsonify(list(nueva_tupla))

# 13-.Ruta para revertir el orden de una tupla y crear una nueva tupla
@app.route('/revertir_tupla', methods=['GET'])
def revertir_tupla():
    if 'tupla' not in request.args:
        request.args['tupla'] = '[]'
    tupla = tuple(json.loads(request.args['tupla']))
    nueva_tupla = tuple(reversed(tupla))
    return jsonify(list(nueva_tupla))

if __name__ == "__main__":
    app.run()

"""
Como Llamar las funciones
1.http://localhost:5000/get_diccionario

2.http://localhost:5000/agregar_clave_valor/<string:clave>/<string:valor>

3.http://localhost:5000/eliminar_clave/<string:clave>

4.http://localhost:5000/modificar_valor/<string:clave>/<string:nuevo_valor>

5.http://localhost:5000/combinar_diccionarios?diccionario2={"alexis":"machado"}

6.http://localhost:5000/agregar_elemento_conjunto/nuevo_elemento?conjunto=["elemento1", "elemento2"]

7.http://localhost:5000/eliminar_elemento_conjunto/elemento_a_eliminar?conjunto=["elemento1", "elemento2", "elemento_a_eliminar"]

8.http://localhost:5000/combinar_conjuntos?conjunto1=["elemento1",%20"elemento2"]&conjunto2=["elemento3",%20"elemento4"]

9.http://localhost:5000/diferencia_entre_conjuntos?conjunto1=["elemento1", "elemento2", "elemento3"]&conjunto2=["elemento2", "elemento3", "elemento4"]

10.http://localhost:5000/agregar_elemento_tupla/elemento_para_agregar/[1, 2, 3]

11.http://localhost:5000/eliminar_elemento_tupla/elemento_a_eliminar?tupla=(1,2,3,4)

12.http://localhost:5000/concatenar_tuplas?tupla1=[1,2,3]&tupla2=[4,5,6]

13.http://localhost:5000/revertir_tupla?tupla=[1,2,3]

"""