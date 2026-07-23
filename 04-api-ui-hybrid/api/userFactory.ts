export interface GeneratedUser {
  name: string;
  email: string;
  password: string;
  title: string;
  birth_date: string;
  birth_month: string;
  birth_year: string;
  firstname: string;
  lastname: string;
  company: string;
  address1: string;
  address2: string;
  country: string;
  zipcode: string;
  state: string;
  city: string;
  mobile_number: string;
}

/**
 * Builds a fresh, unique user payload for automationexercise.com's
 * createAccount API. Each call generates a new email so scenarios
 * can be re-run without colliding with a previous run's account.
 */
export function buildRandomUser(): GeneratedUser {
  const stamp = Date.now();
  return {
    name: `QA Tester ${stamp}`,
    email: `qa.tester.${stamp}@example.com`,
    password: 'SecurePass!123',
    title: 'Mr',
    birth_date: '15',
    birth_month: '6',
    birth_year: '1995',
    firstname: 'QA',
    lastname: `Tester${stamp}`,
    company: 'Automation Labs',
    address1: '221B Baker Street',
    address2: 'Near Test Fixture Lane',
    country: 'India',
    zipcode: '641001',
    state: 'Tamil Nadu',
    city: 'Coimbatore',
    mobile_number: '9876543210',
  };
}
