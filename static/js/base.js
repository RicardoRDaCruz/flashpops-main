var quantidade = Number($(".divmusicas").attr('id').split("_")[1]);
var acertos = dicionario_acertos(quantidade);
for(var i=1;i<quantidade+1;i++){
    posicao=String(i);
    $("#botao-restart"+posicao).click(function() {
        var audio = document.getElementById("audio"+this.id.replace(/botao-restart/g,''));
        audio.currentTime=0;
        audio.play();
    });
    $("#botao-play"+posicao).click(function() {
        var audio = document.getElementById("audio"+this.id.replace(/botao-play/g,''));
        audio.play();
    });
    $("#botao-pause"+String(i)).click(function() {
        var audio = document.getElementById("audio"+this.id.replace(/botao-pause/g,''));
        audio.pause();
    });
    $("#txt"+posicao).click(function(){
        var nomes_separados=this.name.split("_");
        var lista_alternativos = eval(nomes_separados[1]);
        this.addEventListener('input', function(){
            if(this.value.toLowerCase()!=nomes_separados[0]){
                $("#caixa"+this.id.replace(/txt/g,'')).css("background-color","red");
                acertos["acerto"+this.id.replace(/txt/g,'')]=false;
                alterar_placar(acertos, quantidade);
                if(lista_alternativos.includes(this.value.toLowerCase())){
                    $("#caixa"+this.id.replace(/txt/g,'')).css("background-color","green");
                    acertos["acerto"+this.id.replace(/txt/g,'')]=true;
                    alterar_placar(acertos, quantidade);
                } else if(this.value==''){
                    $("#caixa"+this.id.replace(/txt/g,'')).css("background-color","white");
                };
            } else {
                $("#caixa"+this.id.replace(/txt/g,'')).css("background-color","green");
                acertos["acerto"+this.id.replace(/txt/g,'')]=true;
                alterar_placar(acertos, quantidade);                    
            }
        });
    });
}

function alterar_placar(dicionario, numero_total){
    var numero_acertos = 0;
    for(var l=1;l<Object.keys(dicionario).length+1;l++){
        console.log(dicionario["acerto"+l]);
        if(dicionario["acerto"+l]==true){
            numero_acertos+=1;
        }           
    }
    $("#acertos").html("Acertos: "+String(numero_acertos)+" / "+String(numero_total)+" ("+Math.round(100*(numero_acertos/numero_total))+" %)");
}

function dicionario_acertos(numero){
    dicionario = {}
    for(var k=1;k<numero+1;k++){
        dicionario["acerto"+String(k)]=false;
    }
    return dicionario;
}