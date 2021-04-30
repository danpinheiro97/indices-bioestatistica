function inputs() {
  var quantidade = parseInt(window.document.getElementById("inpqt").value);
  var conteudo = "";
  var label = "";
  for (i = 0; i < quantidade; i++) {
    label =
      ' <label class="labels">Digite a quantidade de indivíduos por espécie:<label/><br>';
    conteudo +=
      '<input placeholder="SPC' +
      i +
      '" class="inputs" type="number" onchange="simpson()" name="A' +
      i +
      '"/>';
  }

  document.getElementById("demo").innerHTML = label + conteudo;
}
var especies = [];
var pi = [];

function simpson() {
  var inputs = document.getElementsByClassName("inputs");
  especies = [];
  for (input of inputs) {
    if (input.value !== "") {
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
    simps = 0;
    if (pispc > 0) {
      simps = pispc**2;
    }
    pi.push(simps);
  }
  var totalpi = 0;
  for (p of pi) {
    totalpi += parseFloat(p);
  }
    totalpi = 1 - totalpi;
  document.getElementById("simpsonresultado").value = totalpi;
}


var dados = [];
function salvar_dados() {
  var comu = document.getElementById("inpid");
  dados.push(comu.value);
  dados.push(especies);
  var simpson = document.getElementById("simpsonresultado");
  dados.push(simspon.value);
  console.log(dados);
}

function dados_tabela() {
  var conteudo = "";
  var valorID = parseInt(window.document.getElementById("inpid").value);
  var valorSPC = parseInt(window.document.getElementById("inpqt").value);
  var valorSHA = parseFloat(
    window.document.getElementById("simpsonresultado").value
  );
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


