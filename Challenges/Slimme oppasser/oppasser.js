// function dierenAantal(){
//     giraffenAantal = parseInt(prompt("Hoeveel giraffen zijn er?"));
//     struisvogelAantal = parseInt(prompt("Hoeveel struisvogels zijn er?"));
//     zebraAantal = parseInt(prompt("Hoeveel zebra's zijn er?"));
// }

// function potenBerekening(){
//     if (giraffenAantal > 0){
//         giraffenPoten = giraffenAantal * 4 
//     }
//     else{
//         giraffenPoten = 0
//     }
//     if (struisvogelAantal > 0){
//         struisvogelPoten = struisvogelAantal * 2
//     }
//     else{
//         struisvogelPoten = 0
//     }
//     if (zebraAantal > 0){
//         zebraPoten = zebraAantal * 4
//     }
//     else{
//         zebraPoten = 0
//     }

//     totaalPoten = zebraPoten + struisvogelPoten + giraffenPoten
//     console.log(totaalPoten)
// }
// dierenAantal()
// potenBerekening()

function totaalPoot(){
    const giraffenPoten = 4
    const struisvogelPoten = 2
    const zebraPoten = 4
    giraffenAantal = parseInt(prompt("Hoeveel giraffen zijn er?"));
    struisvogelAantal = parseInt(prompt("Hoeveel struisvogels zijn er?"));
    zebraAantal = parseInt(prompt("Hoeveel zebra's zijn er?"));

    totaalPoten = (giraffenAantal * giraffenPoten) + (struisvogelAantal * struisvogelPoten) + (zebraAantal * zebraPoten)
    console.log("Er zijn",totaalPoten,"dierenpoten")
    document.write("Er zijn", totaalPoten, "dierenpoten")
}
totaalPoot()