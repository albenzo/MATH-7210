data Perm = Perm Int (Int -> Int)

to_list (Perm n f) = map f [1..n]

instance Show Perm where
  show s = show (to_list s)
