function inputs() {
  var quantidade = parseInt(window.document.getElementById("inpqt").value);
  var conteudo = "";
  for (i = 0; i < quantidade; i++) {
    conteudo +=
      '<input placeholder="SPC' +
      i +
      '" class="inputs" type="text" onchange="shannon()" name="A' +
      i +
      '"/>';
  }

  document.getElementById("demo").innerHTML = conteudo;
}
var especies = [];
var pi = [];

function shannon() {
    var inputs = document.getElementsByClassName("inputs");
    especies = [];
    for (input of inputs) {
      if (input.value !== '') {
        especies.push(parseInt(input.value));
      }
    }
  pi = [];
  var total = 0;
  for (especie of especies) {
    total += parseInt(especie);
  }
  var pispc = 0;
  for (especie of especies) {
    pispc = parseInt(especie) / total;
    lnpi = 0;
    if (pispc > 0) {
      lnpi = Math.log(pispc) * pispc;
    }
    pi.push(lnpi);
  }
  var totalpi = 0;
  for (p of pi) {
    totalpi += parseFloat(p);
  }
  totalpi = -1 * totalpi;
  document.getElementById("shannonresultado").value = totalpi;
}

var dados = [];
function salvar_dados(){
  var comu = document.getElementById("inpid");
  dados.push(comu.value);
  dados.push(especies);
  var shannon = document.getElementById("shannonresultado");
  dados.push(shannon.value)
  console.log(dados)

}

function dados_tabela(){
 
  var conteudo = "";
  var valorID = parseInt(window.document.getElementById("inpid").value);
  var valorSPC = parseInt(window.document.getElementById("inpqt").value);
  var valorSHA = parseFloat(window.document.getElementById("shannonresultado").value);
  var lista = [valorID, valorSPC, valorSHA];
  conteudo +=
    "<tr><td>" +
    lista[0] +
    "</td><td>" +
    lista[1] +
    "</td><td>" +
    lista[2] +
    "</td></tr>";
  document.getElementById("tbody").innerHTML += conteudo;


}


