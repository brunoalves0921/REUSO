package me.bruno.framework.repository;

import me.bruno.framework.model.Produto;

import java.util.*;

public class InMemoryRepository<T extends Produto> implements CrudRepository<T> {
    private final Map<Integer, T> storage = new HashMap<>();
    private int currentId = 1;

    @Override
    public void save(T entity) {
        entity.setId(currentId); // Define o ID antes de salvar
        storage.put(currentId++, entity);
    }

    @Override
    public T findById(int id) {
        return storage.get(id);
    }

    @Override
    public void update(int id, T entity) {
        if (storage.containsKey(id)) {
            entity.setId(id); // Mantém o mesmo ID ao atualizar
            storage.put(id, entity);
        }
    }

    @Override
    public void delete(int id) {
        storage.remove(id);
    }

    @Override
    public List<T> findAll() {
        return new ArrayList<>(storage.values());
    }
}
