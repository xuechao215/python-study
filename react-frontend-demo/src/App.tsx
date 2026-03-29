import React, { useState } from 'react';
import ItemList from './components/ItemList';
import { ItemForm } from './components/ItemForm';
import { itemApi } from './lib/api';
import { ItemCreate } from './types';

function App() {
  const [isCreating, setIsCreating] = useState(false);

  const handleCreate = async (data: ItemCreate) => {
    try {
      await itemApi.create(data);
      setIsCreating(false);
      // Trigger refresh (handled inside ItemList for simplicity in this demo,
      // but ideally state should be lifted or use React Query)
      window.location.reload(); 
    } catch (err) {
      console.error(err);
      alert('Failed to create item');
    }
  };

  return (
    <div className="min-h-screen bg-gray-50">
      <header className="bg-white shadow-sm border-b border-gray-200">
        <div className="container mx-auto px-4 py-4 flex justify-between items-center">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 bg-blue-600 rounded-lg flex items-center justify-center text-white font-bold text-xl shadow-md">
              Py
            </div>
            <h1 className="text-xl font-bold text-gray-900 tracking-tight">
              Python Fullstack Demo
            </h1>
          </div>
          <a
            href="http://localhost:8000/docs"
            target="_blank"
            rel="noopener noreferrer"
            className="text-sm font-medium text-gray-600 hover:text-blue-600 transition-colors"
          >
            Backend Docs &rarr;
          </a>
        </div>
      </header>

      <main className="container mx-auto px-4 py-8">
        <ItemList />
      </main>

      {isCreating && (
        <ItemForm
          onSubmit={handleCreate}
          onCancel={() => setIsCreating(false)}
        />
      )}
    </div>
  );
}

export default App;
