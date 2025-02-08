package me.bruno.framework;

import me.bruno.framework.model.Produto;
import me.bruno.framework.repository.InMemoryRepository;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        InMemoryRepository<Produto> produtoRepo = new InMemoryRepository<>();

        while (true) {
            System.out.println("\n=== MENU ===");
            System.out.println("1 - Cadastrar Produto");
            System.out.println("2 - Listar Produtos");
            System.out.println("3 - Buscar Produto por ID");
            System.out.println("4 - Atualizar Produto");
            System.out.println("5 - Remover Produto");
            System.out.println("6 - Sair");
            System.out.print("Escolha uma opção: ");

            int opcao;
            try {
                opcao = Integer.parseInt(scanner.nextLine());
            } catch (NumberFormatException e) {
                System.out.println("Opção inválida! Digite um número.");
                continue;
            }

            switch (opcao) {
                case 1:
                    cadastrarProduto(scanner, produtoRepo);
                    break;
                case 2:
                    listarProdutos(produtoRepo);
                    break;
                case 3:
                    buscarProduto(scanner, produtoRepo);
                    break;
                case 4:
                    atualizarProduto(scanner, produtoRepo);
                    break;
                case 5:
                    removerProduto(scanner, produtoRepo);
                    break;
                case 6:
                    System.out.println("Saindo...");
                    scanner.close();
                    return;
                default:
                    System.out.println("Opção inválida! Tente novamente.");
            }
        }
    }

    private static void cadastrarProduto(Scanner scanner, InMemoryRepository<Produto> repo) {
        System.out.print("Nome do produto: ");
        String nome = scanner.nextLine();

        System.out.print("Preço do produto: ");
        double preco;
        try {
            preco = Double.parseDouble(scanner.nextLine());
        } catch (NumberFormatException e) {
            System.out.println("Preço inválido! Use apenas números.");
            return;
        }

        Produto produto = new Produto(0, nome, preco); // O ID será atribuído no repositório
        repo.save(produto);
        System.out.println("Produto cadastrado com sucesso! ID: " + produto.getId());
    }

    private static void listarProdutos(InMemoryRepository<Produto> repo) {
        System.out.println("\nLista de Produtos:");
        for (Produto p : repo.findAll()) {
            System.out.println("ID: " + p.getId() + " | Nome: " + p.getNome() + " | Preço: R$" + p.getPreco());
        }
    }

    private static void buscarProduto(Scanner scanner, InMemoryRepository<Produto> repo) {
        System.out.print("Digite o ID do produto: ");
        int id;
        try {
            id = Integer.parseInt(scanner.nextLine());
        } catch (NumberFormatException e) {
            System.out.println("ID inválido! Use apenas números.");
            return;
        }

        Produto produto = repo.findById(id);
        if (produto != null) {
            System.out.println("Produto encontrado: " + produto);
        } else {
            System.out.println("Produto não encontrado.");
        }
    }

    private static void atualizarProduto(Scanner scanner, InMemoryRepository<Produto> repo) {
        System.out.print("Digite o ID do produto a ser atualizado: ");
        int id;
        try {
            id = Integer.parseInt(scanner.nextLine());
        } catch (NumberFormatException e) {
            System.out.println("ID inválido! Use apenas números.");
            return;
        }

        if (repo.findById(id) == null) {
            System.out.println("Produto não encontrado.");
            return;
        }

        System.out.print("Novo nome do produto: ");
        String nome = scanner.nextLine();

        System.out.print("Novo preço do produto: ");
        double preco;
        try {
            preco = Double.parseDouble(scanner.nextLine());
        } catch (NumberFormatException e) {
            System.out.println("Preço inválido! Use apenas números.");
            return;
        }

        repo.update(id, new Produto(id, nome, preco));
        System.out.println("Produto atualizado com sucesso!");
    }

    private static void removerProduto(Scanner scanner, InMemoryRepository<Produto> repo) {
        System.out.print("Digite o ID do produto a ser removido: ");
        int id;
        try {
            id = Integer.parseInt(scanner.nextLine());
        } catch (NumberFormatException e) {
            System.out.println("ID inválido! Use apenas números.");
            return;
        }

        if (repo.findById(id) == null) {
            System.out.println("Produto não encontrado.");
            return;
        }

        repo.delete(id);
        System.out.println("Produto removido com sucesso!");
    }
}
