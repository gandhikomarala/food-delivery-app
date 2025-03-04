import { render, screen } from '@testing-library/react';
import App from './App';

test('renders App component', () => {
  render(<App />);
  const linkElement = screen.getByText(/learn react/i);
  expect(linkElement).toBeInTheDocument();
  const headingElement = screen.getByText(/welcome to the food delivery app/i);
  expect(headingElement).toBeInTheDocument();
});
