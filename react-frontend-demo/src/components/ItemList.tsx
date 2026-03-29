import React, { useEffect, useState } from 'react';
import { Item, ItemCreate } from '../types';
import { itemApi } from '../lib/api';
import { Edit2, Trash2, Plus, RefreshCw, AlertCircle } from 'lucide-react';
import { ItemForm } from './ItemForm';

export default function ItemList() {
  const [items, setItems] = useState<Item[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [editingItem, setEditingItem] = useState<Item | null>(null);
  const [isCreating, setIsCreating] = useState(false);

  // Fetch Items
  const fetchItems = async () => {
    setLoading(true);
    setError(null);
    try {
      const response = await itemApi.getAll();
      setItems(response.data);
    } catch (err: any) {
      setError('Failed to fetch items. Is the backend running?');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchItems();
  }, []);

  // Handle Create
  const handleCreate = async (data: ItemCreate) => {
    try {
      await itemApi.create(data);
      setIsCreating(false);
      fetchItems();
    } catch (err) {
      setError('Failed to create item');
    }
  };

  // Handle Update
  const handleUpdate = async (id: number, data: ItemCreate) => {
    try {
      await itemApi.update(id, data);
      setEditingItem(null);
      fetchItems();
    } catch (err) {
      setError('Failed to update item');
    }
  };

  // Handle Delete
  const handleDelete = async (id: number) => {
    if (!window.confirm('Are you sure you want to delete this item?')) return;
    try {
      await itemApi.delete(id);
      fetchItems();
    } catch (err) {
      setError('Failed to delete item');
    }
  };

  return (
    <div className="container mx-auto px-4 py-8 max-w-4xl">
      <div className="flex justify-between items-center mb-8">
        <h1 className="text-3xl font-bold text-gray-900">Python + React CRUD</h1>
        <button
          onClick={() => setIsCreating(true)}
          className="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-lg flex items-center gap-2 transition-colors shadow-sm"
        >
          <Plus size={20} />
          New Item
        </button>
      </div>

      {error && (
        <div className="bg-red-50 text-red-700 p-4 rounded-lg mb-6 flex items-center gap-2 border border-red-200">
          <AlertCircle size={20} />
          {error}
        </div>
      )}

      {loading && items.length === 0 ? (
        <div className="text-center py-12 text-gray-500">
          <RefreshCw className="animate-spin mx-auto mb-2" size={32} />
          Loading items...
        </div>
      ) : (
        <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
          {items.map((item) => (
            <div
              key={item.id}
              className="bg-white rounded-xl shadow-sm border border-gray-100 hover:shadow-md transition-shadow p-5 flex flex-col justify-between"
            >
              <div>
                <div className="flex justify-between items-start mb-2">
                  <h3 className="font-semibold text-lg text-gray-800 truncate" title={item.title}>
                    {item.title}
                  </h3>
                  <span className={`px-2 py-0.5 text-xs rounded-full ${item.is_active ? 'bg-green-100 text-green-700' : 'bg-gray-100 text-gray-600'}`}>
                    {item.is_active ? 'Active' : 'Inactive'}
                  </span>
                </div>
                <p className="text-gray-500 text-sm mb-4 line-clamp-2 h-10">
                  {item.description || 'No description provided'}
                </p>
                <div className="flex items-baseline gap-1 text-gray-900 mb-4">
                  <span className="text-2xl font-bold">${item.price}</span>
                  {item.tax && (
                    <span className="text-xs text-gray-500">+ ${item.tax} tax</span>
                  )}
                </div>
              </div>

              <div className="flex justify-end gap-2 pt-4 border-t border-gray-50">
                <button
                  onClick={() => setEditingItem(item)}
                  className="p-2 text-gray-600 hover:text-blue-600 hover:bg-blue-50 rounded-md transition-colors"
                  title="Edit"
                >
                  <Edit2 size={18} />
                </button>
                <button
                  onClick={() => handleDelete(item.id)}
                  className="p-2 text-gray-600 hover:text-red-600 hover:bg-red-50 rounded-md transition-colors"
                  title="Delete"
                >
                  <Trash2 size={18} />
                </button>
              </div>
            </div>
          ))}
        </div>
      )}

      {items.length === 0 && !loading && (
        <div className="text-center py-12 bg-gray-50 rounded-lg border-2 border-dashed border-gray-200">
          <p className="text-gray-500 mb-4">No items found yet.</p>
          <button
            onClick={() => setIsCreating(true)}
            className="text-blue-600 font-medium hover:underline"
          >
            Create your first item
          </button>
        </div>
      )}

      {/* Modals */}
      {isCreating && (
        <ItemForm
          onSubmit={handleCreate}
          onCancel={() => setIsCreating(false)}
        />
      )}

      {editingItem && (
        <ItemForm
          initialData={editingItem}
          onSubmit={(data) => handleUpdate(editingItem.id, data)}
          onCancel={() => setEditingItem(null)}
        />
      )}
    </div>
  );
}
