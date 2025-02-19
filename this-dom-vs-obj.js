
    // this com DOM
// Suponha que exista um botão no HTML: <button>Clique aqui</button>
Document.querySelectotr("button").addEventListener("click", function(){
    console.log(this) //--> 'this aqui se refere ao botão clicado

});

    // ----------------------------------------

    // this  em um objeto
const obj = {
    nome: "JavaScript",
    mostrarThis: function () {
        console.log(this); //--> refere-se  ao próprio objeto 'obj'
    }
}

//Chamando o método de objeto, 'this' aqui se refere ao objeto
obj.mostrarThis();


    // --------------------------------------
// Criando um escopo externo para a arrow function
const escopoGlobal = {
    nome: "Escopo Global",
    mostrarThis: function () {
        console.log(this); // --> aqui 'this' serefere ao objeto 'escopoGlobal
    }
};

const obj1 = {
    nome: "Objeto",
    mostrarThis () => {
        console.log(this); // --> aqui 'this' não se refere ao objeto, mas sim so escopo externo (global)
    }

};

//Chamando as funções
escopoGlobal,mostrarThis(); // aqui o 'this' refere ao objeto 'escopoGlobal
obj1.mostrarThis(); // aqui o 'this' se refere ao escopoglobal, não ao objeto 'obj1'