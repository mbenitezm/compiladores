# Marcel Benítez 1139855
# Tarea de implementación de estructuras de datos

# Estructura de stack

class Stack():
  # Inicialización del stack con tamaño 0 y un arreglo vacío.
  def __init__(self):
    self.list = []
    self.size = 0

  # Regresa vacío si el tamaño del arreglo es 0
  def isEmpty(self):
    if self.size == 0:
      return True
      print ("The Stack is empty")
    else:
      return False
      print ("The stack is not empty")

  # Agrega un elemento al arreglo y se incrementa el tamaño 
  def push(self, node):
    self.list.append(node)
    self.size+= 1
    print ("Element added")

  # En caso de que la lista esté vacía, se elimina el ultimo elemento agregado
  def pop(self):
    if not self.isEmpty():
      del self.list[self.size-1]
      self.size-= 1
      print ("Element removed")
    else:
      print ("The Stack is empty")

  # Regresa el tamaño actual de la lista del stack
  def length(self):
    print (str(self.size))

  # Regresa el último elemento agregado a la lista del stack
  def peek(self):
    if not self.isEmpty():
      print (self.list[self.size-1])
    else:
      print ("The Stack is empty")

  # Se pasa por cada elemento del arreglo del stack, comparandose con el
  # elemento que se está buscando.
  def search(self, node):
    for element in self.list:
      if element == node:
        print ("found")
        return
    print ("not found")

stack = Stack()
stack.pop()
stack.peek()
stack.isEmpty()
stack.push(3)
stack.push(4)
stack.push(7)
stack.isEmpty()
stack.peek()
stack.pop()
stack.peek()
stack.length()
stack.search(7)
stack.search(4)

# Estructura de Queue

class Queue():
  # Inicialización del stack con tamaño 0 y un arreglo vacío.
  def __init__(self):
    self.list = []
    self.size = 0

  # Regresa vacío si el tamaño del arreglo es 0
  def isEmpty(self):
    if self.size == 0:
      return True
      print ("The Queue is empty")
    else:
      return False
      print ("The Queue is not empty")

  # Agrega un elemento al arreglo y se incrementa el tamaño 
  def push(self, node):
    self.list.append(node)
    self.size+= 1
    print ("Element added")

  # En caso de que la lista esté vacía, se elimina el primer elemento agregado
  def pop(self):
    if not self.isEmpty():
      del self.list[0]
      self.size-= 1
      print ("Element removed")
    else:
      print ("The Queue is empty")

  # Regresa el tamaño actual de la lista del stack
  def length(self):
    print (str(self.size))

  # Regresa el primer elemento agregado a la lista del stack
  def front(self):
    if not self.isEmpty():
      print (self.list[0])
    else:
      print ("The Queue is empty")

  # Se pasa por cada elemento del arreglo del stack, comparandose con el
  # elemento que se está buscando.
  def search(self, node):
    for element in self.list:
      if element == node:
        print ("found")
        return
    print ("not found")
print ("------------------------------------------------------------")
queue = Queue()
queue.pop()
queue.front()
queue.isEmpty()
queue.push(3)
queue.push(4)
queue.push(7)
queue.isEmpty()
queue.front()
queue.pop()
queue.front()
queue.pop()
queue.front()
queue.length()
queue.search(7)
queue.search(4)

# Implementación de estructura binary tree
# Se tendrá una clase TreeNode la cual tendra el valor actual del arbol y
# apuntadores a la derecha y a la izquierda.
class TreeNode():
  def __init__(self, value):
    self.left = None  #Nulo es None
    self.right = None
    self.value = value
    self.size = 1

# Método de agregar un valor
# Recursivamente se comparará el valor que se quiere agregar con los valores
# Que están en el arbol.
# Si el valor que se quiere agregar es mayor al nodo en que se encuentra en dado
# momento se revisa si existen un nodo al a derecha. Si no hay se creará un nodo
# nuevo y se enlaza con self.right, de lo contrario se llama recursivamente a la
# función con el siguiente nodo.
  def insert(self, value):
    if self.size == 0:
      self.size += 1
      self.value = value
      print ("Element added")
    else: 
      if value > self.value:
        if self.right is None:
          self.right = TreeNode(value)
          self.size += 1
          print ("Element added")
        else:
          self.right.insert(value)
      elif value < self.value:
        if self.left is None:
          self.left = TreeNode(value)
          self.size += 1
          print ("Element added")
        else:
          self.left.insert(value)

  # Método buscar un valor
  # De la misma forma que con agregar valor, si visitan los nodos del arbol
  # recursivamente. En lugar de comparar por desigualdades, se compara primero
  # con el nodo actual el valor buscado. Si es encontrado se regresa true, de lo
  # contrario se realizan las desigualdades mencionadas en el método de agregar
  # valor
  def find(self, value):
    if self.value == value:
      print ("Found!")
      return
    else:
      if value > self.value:
        if self.right is not None:
          self.right.find(value)
      elif value < self.value:
        if self.left is not None:
          self.left.find(value)

  # Método de imprimir un valor
  # Se visita todo el arbol recursivamente en preorden
  def preorder(self):
    print (self.value)
    if self.left is not None:
      self.left.preorder()
    if self.right is not None:
      self.right.preorder()

print ("---------------------------------------------------")
tree = TreeNode(5)
tree.insert(1)
tree.insert(2)
tree.insert(7)
tree.insert(6)
tree.find(5)
tree.find(7)
tree.find(10)
tree.preorder()
