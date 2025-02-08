package me.bruno.framework.repository;

import java.util.List;

public interface CrudRepository<T> {
    void save(T entity);
    T findById(int id);
    void update(int id, T entity);
    void delete(int id);
    List<T> findAll();
}
