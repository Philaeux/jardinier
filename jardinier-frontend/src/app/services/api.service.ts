import { Injectable } from '@angular/core'
import { Apollo } from "apollo-angular"
import { QUERY_SUCCESS_EXAMPLE } from '../models/queries'
import { ResponseQuerySuccessExample } from '../models/queries'

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  /**
   * Example of access to the backend
   * @param apollo 
   */

  constructor(private apollo: Apollo) { }

  /**
   * Query example to the graphql backend
   */
  querySuccessExample() {
    return this.apollo.query<ResponseQuerySuccessExample>({
        query: QUERY_SUCCESS_EXAMPLE,
        fetchPolicy: 'network-only'
    })
  }
}
