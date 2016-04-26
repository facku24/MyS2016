module Language.ListAssoc where

data ListAssoc a b = Empty
                   | Node a b (ListAssoc a b)
    deriving Show

la_buscar :: Eq a => ListAssoc a b -> a -> Maybe b
la_buscar Empty _ = Nothing
la_buscar (Node a b l) a' | a == a'   = Just b
                          | otherwise = la_buscar l a'

la_agregar :: Eq a => a -> b -> ListAssoc a b -> ListAssoc a b
la_agregar a b Empty = Node a b Empty
la_agregar a b (Node a' b' l) | a == a'   = Node a' b l
                              | otherwise = Node a' b' (la_agregar a b l)






