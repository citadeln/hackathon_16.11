package main

import (
	"database/sql"
	"fmt"
	"io"
	"os"

	_ "github.com/lib/pq"
)

type product struct {
	id       int
	name     string
	obj_type int8
}

func main() {

	connStr := "user=dima password=qwe dbname=hackaton sslmode=disable"
	db, err := sql.Open("postgres", connStr)
	if err != nil {
		panic(err)
	}
	defer db.Close()
	file, err := os.Open("./DB/fakt.txt")
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
	defer file.Close()

	data := make([]byte, 64)

	for {
		n, err := file.Read(data)
		if err == io.EOF { // если конец файла
			break // выходим из цикла
		}
		// fmt.Print(string(data[:n]))

		db.Exec(string(data[:n]))
		if err != nil {
			panic(err)
		}
	}

	// rows, err := db.Query("select * from objects where type=5")
	// if err != nil {
	// 	panic(err)
	// }
	// defer rows.Close()
	// products := []product{}

	// for rows.Next() {
	// 	p := product{}
	// 	err := rows.Scan(&p.id, &p.name, &p.obj_type)
	// 	if err != nil {
	// 		fmt.Println(err)
	// 		continue
	// 	}
	// 	products = append(products, p)
	// }
	// for _, p := range products {
	// 	fmt.Println(p.id, p.name)
	// }

}
