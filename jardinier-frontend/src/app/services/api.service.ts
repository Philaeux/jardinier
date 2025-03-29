import { Injectable } from '@angular/core'
import { Apollo, gql } from "apollo-angular"
import { Measure } from '../models'

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  constructor(private apollo: Apollo) { }

  measures(limit: number, offset: number) {
    return this.apollo.query<{
      measures: [Measure]
    }>({
      query: gql`
query Measures($limit: Int!, $offset: Int!) {
  measures(limit: $limit, offset: $offset, orderBy: {time: DESC}){
    time
    temperature
    humidity
  }
}
        `,
      fetchPolicy: 'network-only',
      variables: {
        limit: limit,
        offset: offset
      }
    })
  }
}
