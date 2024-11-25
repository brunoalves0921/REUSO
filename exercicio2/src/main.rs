use std::f64;

fn main() {
    // Definindo duas tuplas que representam os pontos (x, y, z)
    let ponto_a = (1.0, 2.0, 3.0);
    let ponto_b = (4.0, 5.0, 6.0);

    // Calculando a distância euclidiana entre os pontos
    let distancia = distancia_euclidiana(ponto_a, ponto_b);

    // Exibindo o resultado
    println!("A distância euclidiana entre os pontos é: {:.2}", distancia);
}

// Função para calcular a distância euclidiana entre dois pontos em 3D
fn distancia_euclidiana(p1: (f64, f64, f64), p2: (f64, f64, f64)) -> f64 {
    ((p2.0 - p1.0).powi(2) + (p2.1 - p1.1).powi(2) + (p2.2 - p1.2).powi(2)).sqrt()
}
