import { render, screen } from '@testing-library/react';
import App from '../App';

describe('App component', () => {
  test('affiche le titre Liste des employés', () => {
    render(<App />);
    const title = screen.getByText(/liste des employés/i);
    expect(title).toBeInTheDocument();
  });
});
