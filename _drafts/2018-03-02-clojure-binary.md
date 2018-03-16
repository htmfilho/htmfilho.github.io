## Binary to string

(def bin-sentence (.getLatestPost JimHerron))

(apply str
       (reduce conj
               []
               (map #(char (Integer/parseInt % 2))
                    (.split bin-sentence " "))))


