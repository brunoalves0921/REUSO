// ALUNO: Jorge Bruno Costa Alves
// MATRICULA: 509718
use std::io;

// Função que calcula a média dos números positivos em um array de 10 elementos
fn media_positivos(numeros: [i32; 10]) -> Option<f64> {
    // Filtra apenas os números positivos do array, copiando-os para um vetor `positivos`
    let positivos: Vec<i32> = numeros.iter().cloned().filter(|&x| x > 0).collect();
    
    // Verifica se o vetor `positivos` está vazio, retornando None se não houver números positivos
    if positivos.is_empty() {
        None
    } else {
        // Calcula a soma dos elementos positivos e divide pelo número de elementos para obter a média
        let soma: i32 = positivos.iter().sum();
        let media = soma as f64 / positivos.len() as f64;
        Some(media) // Retorna a média como Some(f64)
    }
}

// Função que calcula o produto dos números pares do array
fn produto_pares(numeros: [i32; 10]) -> i32 {
    // Itera sobre o array e filtra os números pares (exclui zero) com filter(|&&x| x % 2 == 0 && x != 0)
    // Depois, calcula o produto dos números pares usando `product()`
    numeros.iter().filter(|&&x| x % 2 == 0 && x != 0).product()
}

// Função principal para a Questão 1, chama as funções de média e produto e exibe os resultados
fn questao_01_main() {
    let numeros = [3, 2, 12, 33, 5, 23, 6, 7, 8, 9];
    
    // Calcula e exibe a média dos números positivos no array
    match media_positivos(numeros) {
        Some(media) => println!("Média dos números positivos: {}", media),
        None => println!("Não há números positivos."),
    }
    
    // Calcula e exibe o produto dos números pares no array
    let produto = produto_pares(numeros);
    println!("Produto dos números pares: {}", produto);
}

// Função que lê um valor inteiro do teclado e retorna
fn ler_inteiro() -> i32 {
    let mut entrada = String::new();
    io::stdin().read_line(&mut entrada).expect("Falha ao ler a entrada");
    entrada.trim().parse().expect("Por favor, insira um número inteiro")
}

// Função que recebe uma tupla de três inteiros e retorna uma tupla com:
// - Soma dos três números
// - Maior número
// - Menor número
fn analisar_tupla(valores: (i32, i32, i32)) -> (i32, i32, i32) {
    let soma = valores.0 + valores.1 + valores.2; // Soma dos três elementos da tupla
    let maior = *[valores.0, valores.1, valores.2].iter().max().unwrap(); // Maior elemento
    let menor = *[valores.0, valores.1, valores.2].iter().min().unwrap(); // Menor elemento
    (soma, maior, menor) // Retorna uma tupla com (soma, maior, menor)
}

// Função principal para a Questão 2, solicita três números, analisa a tupla e exibe os resultados
fn questao_02_main() {
    println!("Insira o primeiro número inteiro:");
    let a = ler_inteiro();
    println!("Insira o segundo número inteiro:");
    let b = ler_inteiro();
    println!("Insira o terceiro número inteiro:");
    let c = ler_inteiro();
    
    let tupla = (a, b, c);
    let resultado = analisar_tupla(tupla);
    println!("Soma: {}, Maior: {}, Menor: {}", resultado.0, resultado.1, resultado.2);
}

// Função main que permite ao usuário escolher entre as duas questões, ou sair do programa
fn main() {
    loop {
        println!("Escolha a questão que deseja responder (1 ou 2) ou digite 0 para sair:");
        let escolha = ler_inteiro();
        
        // Verifica a escolha do usuário e chama a função correspondente
        match escolha {
            1 => questao_01_main(), // Executa a Questão 1
            2 => questao_02_main(), // Executa a Questão 2
            0 => {
                println!("Saindo..."); // Encerra o loop e finaliza o programa
                break;
            },
            _ => println!("Opção inválida, por favor escolha 1, 2 ou 0."), // Tratamento de erro para opções inválidas
        }
    }
}
