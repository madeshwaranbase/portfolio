import axios from 'axios';
import { GeneratedUser } from './userFactory';

const BASE_URL = 'https://automationexercise.com/api';

export class AccountApiClient {
  /**
   * POST /createAccount
   * responseCode 201 = created, 400 = email already exists.
   */
  async createAccount(user: GeneratedUser): Promise<number> {
    const params = new URLSearchParams(user as unknown as Record<string, string>);
    const response = await axios.post(`${BASE_URL}/createAccount`, params);
    return response.data.responseCode;
  }

  /**
   * DELETE /deleteAccount
   * The API expects email/password as a form-encoded body, not a query
   * string — axios's `params` option puts them in the URL instead, which
   * this API rejects with responseCode 400. Send them as `data` instead,
   * same as createAccount.
   * responseCode 200 = deleted, 404 = account not found.
   */
  async deleteAccount(email: string, password: string): Promise<number> {
    const body = new URLSearchParams({ email, password });
    const response = await axios.delete(`${BASE_URL}/deleteAccount`, { data: body });
    return response.data.responseCode;
  }
}