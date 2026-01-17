// {{ComponentName}}.spec.tsx
import { render, screen } from '@testing-library/react';
import { {{ComponentName}} } from './{{ComponentName}}';

describe('{{ComponentName}}', () => {
  it('renders without crashing', () => {
    render(<{{ComponentName}} />);
    expect(screen.getByTestId('{{component-name}}')).toBeInTheDocument();
  });

  // TODO: Add more test cases
});
