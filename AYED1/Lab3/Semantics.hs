module Language.Semantics where

import Language.Syntax
import Language.ListAssoc

-- Asignación de valores para las variables enteras
type StateI = ListAssoc VarName Int
-- Asignación de valores para las variables booleanas
type StateB = ListAssoc VarName Bool

defaultIntValue :: Int
defaultIntValue = 0

defaultBoolValue :: Bool
defaultBoolValue = True

-- Tipo que representa la continuación de un paso de ejecución.
-- Ésta puede ser: Falta ejecutar una sentencia (ToExec), o ya no hay nada por
-- ejecutar (Finish).
data Continuation = ToExec Statement
                  | Finish


-- El estado consta del valor de las variables enteras y las booleanas
type State = (StateI,StateB)


evalIExpr :: IntExpr -> StateI -> Int
evalIExpr (ConstI i) _ = i
evalIExpr (VI v) st = maybe (error $ "la variable " ++ show v ++ " no está declarada")
                            id (la_buscar st v)
evalIExpr (Neg e) st = - (evalIExpr e st)
evalIExpr (Plus e1 e2) st = (evalIExpr e1 st) + (evalIExpr e2 st)
evalIExpr (Prod e1 e2) st = (evalIExpr e1 st) * (evalIExpr e2 st)
evalIExpr (Div e1 e2) st = (evalIExpr e1 st) `div` (evalIExpr e2 st)
evalIExpr (Mod e1 e2) st = (evalIExpr e1 st) `mod` (evalIExpr e2 st)


-- Para evaluar las expresiones booleanas
-- necesitamos también el estado de variables enteras
-- porque en Equal y Less tenemos subexpresiones enteras.
evalBExpr :: BoolExpr -> State -> Bool
evalBExpr (ConstB b) _ = b
evalBExpr (VB v) st = maybe (error $ "la variable " ++ show v ++ " no está declarada")
                           id (la_buscar (snd st) v)
evalBExpr (Not e) st = not (evalBExpr e st)
evalBExpr (And e1 e2) st = (evalBExpr e1 st) && (evalBExpr e2 st)
evalBExpr (Or e1 e2) st = (evalBExpr e1 st) || (evalBExpr e2 st)
evalBExpr (Equal e1 e2) st = (evalIExpr e1 $ fst st) == (evalIExpr e2 $ fst st)
evalBExpr (Less e1 e2) st = (evalIExpr e1 $ fst st) < (evalIExpr e2 $ fst st)

-- Evaluar un paso de ejecución en un programa.
evalStep :: Statement -> State -> (State , Continuation)
evalStep Skip st = (st , Finish)
evalStep (AssignI (Var v IntT) e) (sti,stb) = 
    ((la_agregar v (evalIExpr e sti) sti,stb) , Finish)
evalStep (AssignB (Var v BoolT) e) st@(sti,stb) = 
    ((sti,la_agregar v (evalBExpr e st) stb) , Finish)
evalStep (Seq stmt1 stmt2) st =
    let (st',cont1) = evalStep stmt1 st 
    in
        case cont1 of
             ToExec stmt1' -> (st' , ToExec (Seq stmt1' stmt2))
             Finish        -> (st' , ToExec stmt2)
evalStep (If []) st = error "Ninguna guarda es verdadera"
evalStep (If ((be,stmt):cs)) st 
    | evalBExpr be st = (st , ToExec stmt)
    | otherwise      = (st , ToExec (If cs))
evalStep (Do be stmt) st 
    | evalBExpr be st = (st , ToExec (Seq stmt (Do be stmt)))
    | otherwise      = (st , Finish)

