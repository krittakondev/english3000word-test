package main

import (
	"fmt"
	"io"
	"net/http"
	"os"
	"strings"
)

func searchImg(word string) {
	url := fmt.Sprintf("https://www.google.com/search?q=%s&tbm=isch", word)
	resp, err := http.Get(url)
	if err != nil {
		panic(err)
	}
	body, err := io.ReadAll(resp.Body)
	resp.Body.Close()
	if err != nil {
		panic(err)
	}
	fmt.Println(string(body))

}

func main() {
	fmt.Println("testing")
	b_words, err := os.ReadFile("./3000word.txt")
	if err != nil {
		panic(err)
	}

	words := strings.Split(string(b_words), "\n")
	for i, v := range words {
		fmt.Printf("%d => %s\n", i, v)
	}
	searchImg("banana")
	// url := fmt.Sprintf("https://www.google.com/search?q=%s&tbm=isch", "test")
	// http.NewRequest("GET", url)
}
