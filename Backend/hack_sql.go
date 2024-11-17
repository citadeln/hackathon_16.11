package main

import (
	"database/sql"
	"fmt"
	"html/template"
	"log"
	"net/http"

	_ "github.com/lib/pq"
)

type Top_wells struct {
	id      int
	xz_name string
	craft   int
}

// type msg string
var database *sql.DB

func IndexHandler(w http.ResponseWriter, r *http.Request) {

	rows, err := database.Query("select * from objects where type=5")
	if err != nil {
		log.Println(err)
	}
	defer rows.Close()
	top_wells := []Top_wells{}

	for rows.Next() {
		k := Top_wells{}
		err := rows.Scan(&k.id, &k.xz_name, &k.craft)
		if err != nil {
			fmt.Println(err)
			continue
		}
		top_wells = append(top_wells, k)
	}

	tmpl, _ := template.ParseFiles("front/index.html")
	tmpl.Execute(w, top_wells)
	// for _, p := range top_wells {
	// 	fmt.Println(p.id, p.xz_name, p.craft)
	// }
}

func main() {

	connStr := "user=dima password=qwe dbname=hackaton sslmode=disable"
	db, err := sql.Open("postgres", connStr)
	if err != nil {
		panic(err)
	}

	database = db

	defer db.Close()

	rows, err := db.Query("select * from objects where type=5")
	if err != nil {
		panic(err)
	}
	defer rows.Close()
	top_wells := []Top_wells{}

	for rows.Next() {
		p := Top_wells{}
		err := rows.Scan(&p.id, &p.xz_name, &p.craft)
		if err != nil {
			fmt.Println(err)
			continue
		}
		top_wells = append(top_wells, p)
	}
	for _, p := range top_wells {
		fmt.Println(p.id, p.xz_name, p.craft)
	}

	http.HandleFunc("/", IndexHandler)
	fmt.Println("Server is listening...")
	http.ListenAndServe("localhost:8181", nil)
}
