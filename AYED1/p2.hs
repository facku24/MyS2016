data Titulo = Ducado | Marquesado | Condado | Vizcondado | Baronia
-- Ejercicio 2: TIPOS ENUMERADOS
hombre :: Titulo -> String
hombre Ducado = "Duque"
hombre Marquesado = "Marques"
hombre Condado = "Conde"
hombre Vizcondado = "Vizconde"
hombre Baronia = "Baron"

dama :: Titulo -> String
dama Ducado = "Duquesa"
dama Marquesado = "Marquesa"
dama Condado = "Condesa"
dama Vizcondado = "Vizcondesa"
damad Baronia = "Barona"

-- EJERCICIO 3: TIPOS ENUMERADOS; CONSTRUCTORES CON ARGUMENTOS
type Territorio = String
type Nombre = String
type Gen 	= String

masculino, femenino :: Gen
masculino = "Masculino"
femenino = "Femenino"

data Persona = Rey Gen						-- constructor sin argumento
			| Noble Gen Titulo Territorio	-- constructor con dos argumentos
			| Caballero Gen Nombre			-- constructor con un argumento
			| Aldeano Nombre				-- constructor con un argumento

tratamiento :: Persona -> String
tratamiento (Rey genero) | genero == "Masculino" = "Su majestad el rey"
						 | otherwise = "Su majestad la reina"
tratamiento (Noble gen tit ter) | gen == "Masculino" = "El " ++ hombre tit ++ " de " ++ ter
								| otherwise = "La " ++ dama tit ++ " de " ++ ter
tratamiento (Caballero gen nombre) | gen == "Masculino" = "Sir " ++ nombre
								   | otherwise = "Dame " ++ nombre
tratamiento (Aldeano nombre) = nombre

sirs :: [Persona] -> [String]
sirs[] = []
sirs ((Caballero gen nombre):xs) = nombre : (sirs (xs))
sirs (x:xs) = sirs xs

is_sirs :: Persona -> Bool
is_sirs (Caballero gen nombre) = True
is_sirs persona = False

mayor2 :: Int -> Bool
mayor2 x = x > 2

--sirs2 :: [Persona] -> [String]
--sirs2 [] = []
--sirs2 xs = filter is_sirs xs

-- EJERCICIO 4: TIPOS RECURSIVOS
data IntExp = Const Int 			-- constante
			| Op IntExp				-- opuesto
			| Plus IntExp IntExp	-- suma
			| Times IntExp IntExp	-- multiplicacion
			| Div IntExp IntExp		-- division

eval :: IntExp -> Int
eval (Const a) 	= a
eval (Op a) 	= - eval (a)
eval (Plus a b) = (+) (eval a) (eval b)
eval (Times a b)= (*) (eval a) (eval b)
eval (Div a b)	= div (eval a) (eval b)

substract :: IntExp -> IntExp -> IntExp
substract a b | (eval a) > (eval b) = (Plus a (Op b))
			  | otherwise = (Op (Plus b (Op a)))

data BoolExp = Constb Bool
			| Not BoolExp
			| And BoolExp BoolExp
			| Or BoolExp BoolExp

evalb :: BoolExp -> Bool
evalb (Constb a) = a
evalb (Not b) 	 = not (evalb b)
evalb (And a b)  = (evalb a) && (evalb b)
evalb (Or a b) 	 = (evalb a) || (evalb b)

--EJERCICIO 5: TIPOS RECURSIVOS Y POLIMÓRFICOS
data ListAssoc a b = Empty | Node a b (ListAssoc a b)

type Diccionario = ListAssoc String String
type Padron 	 = ListAssoc Int String
type Telefonica  = ListAssoc String Int

