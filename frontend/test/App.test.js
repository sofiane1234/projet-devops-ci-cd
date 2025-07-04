import { render, screen, waitFor } from '@testing-library/react';
import App from '../src/App';

beforeEach(() => {
  global.fetch = jest.fn(() =>
    Promise.resolve({
      ok: true,
      json: () =>
        Promise.resolve([
          { id: 1, name: 'Alice', role: 'Engineer' },
          { id: 2, name: 'Bob', role: 'Manager' },
        ]),
    })
  );
});

afterEach(() => {
  jest.clearAllMocks();
});

describe('App component', () => {
  test('affiche le titre Liste des employés', () => {
    render(<App />);
    const title = screen.getByText(/liste des employés/i);
    expect(title).toBeInTheDocument();
  });

  test('affiche les employés après le fetch', async () => {
    render(<App />);

    await waitFor(() => {
      expect(screen.getByText(/Alice/i)).toBeInTheDocument();
      expect(screen.getByText(/Engineer/i)).toBeInTheDocument();
      expect(screen.getByText(/Bob/i)).toBeInTheDocument();
      expect(screen.getByText(/Manager/i)).toBeInTheDocument();
    });
  });

  test('affiche un message de chargement pendant le fetch', () => {
    render(<App />);
    const loading = screen.getByText(/chargement/i);
    expect(loading).toBeInTheDocument();
  });
});
