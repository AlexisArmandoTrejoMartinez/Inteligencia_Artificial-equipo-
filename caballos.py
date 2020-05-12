# Integrantes:
# Hidalgo Hernandez Juan Daniel
# Trejo Martinez Alexis Armando

N = 8

def valida(i, j, sol):
  if (i>=1 and i<=N and j>=1 and j<=N):
    if (sol[i][j]==-1):
      return True
  return False

def Camino_caballero(sol, i, j, step_count, x_move, y_move):
  if (step_count == N*N):
    return True

  for k in range(0, 8):
    next_i = i+x_move[k]
    next_j = j+y_move[k]

    if(valida(next_i, next_j, sol)):
      sol[next_i][next_j] = step_count
      if (Camino_caballero(sol, next_i, next_j, step_count+1, x_move, y_move)):
        return True
      sol[next_i][next_j] = -1;

  return False

def inicia():
  sol = []

  for i in range(0, N+1):
    a = [0]+([-1]*N)
    sol.append(a)

  x_move = [2, 1, -1, -2, -2, -1, 1, 2]
  y_move = [1, 2, 2, 1, -1, -2, -2, -1]

  sol[1][1] = 0

  if (Camino_caballero(sol, 1, 1, 1, x_move, y_move)):
    for i in range(1, N+1):
      print(sol[i][1:])
    return True
  return False

if __name__ == '__main__':
  print(inicia())
