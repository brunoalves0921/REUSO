package me.bruno.framework.repository;

import java.io.*;
import java.util.*;

public class InFileRepository<T> implements CrudRepository<T>, Serializable {
    private final String filePath;
    private Map<Integer, T> storage = new HashMap<>();
    private int currentId = 1;

    public InFileRepository(String filePath) {
        this.filePath = filePath;
        loadFromFile();
    }

    @Override
    public void save(T entity) {
        storage.put(currentId++, entity);
        saveToFile();
    }

    @Override
    public T findById(int id) {
        return storage.get(id);
    }

    @Override
    public void update(int id, T entity) {
        if (storage.containsKey(id)) {
            storage.put(id, entity);
            saveToFile();
        }
    }

    @Override
    public void delete(int id) {
        storage.remove(id);
        saveToFile();
    }

    @Override
    public List<T> findAll() {
        return new ArrayList<>(storage.values());
    }

    private void saveToFile() {
        try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(filePath))) {
            oos.writeObject(storage);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private void loadFromFile() {
        try (ObjectInputStream ois = new ObjectInputStream(new FileInputStream(filePath))) {
            storage = (Map<Integer, T>) ois.readObject();
            currentId = storage.size() + 1;
        } catch (IOException | ClassNotFoundException e) {
            storage = new HashMap<>();
        }
    }
}
