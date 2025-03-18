import { ApplicationConfig, inject, provideZoneChangeDetection } from '@angular/core';
import { provideRouter } from '@angular/router';

import { routes } from './app.routes';

import { provideHttpClient } from '@angular/common/http';
import { ApolloClientOptions, ApolloLink, InMemoryCache } from '@apollo/client/core';
import { setContext } from '@apollo/client/link/context';
import { Apollo, APOLLO_OPTIONS } from 'apollo-angular';
import { HttpLink } from 'apollo-angular/http';

const uri = 'http://127.0.0.1:5000/graphql'

export function apolloOptionsFactory(): ApolloClientOptions<any> {
  const httpLink = inject(HttpLink)

  const basic = setContext((operation, context) => ({
    headers: {
      Accept: 'charset=utf-8'
    },
  }))

  const auth = setContext((operation, context) => {
    const token = localStorage.getItem('token') // Save token in the local storage if you want it in the header

    if (token === null) {
      return {}
    } else {
      return {
        headers: {
          Authorization: `Bearer ${token}`, // Token is sent in the header, check it in the backend
        },
      }
    }
  })

  return {
    link: ApolloLink.from([
      basic,
      auth,
      httpLink.create({
        uri: uri
      })]),
    cache: new InMemoryCache(),
  }
}

export const graphqlProvider: ApplicationConfig['providers'] = [
  Apollo,
  {
    provide: APOLLO_OPTIONS,
    useFactory: apolloOptionsFactory,
  },
]



export const appConfig: ApplicationConfig = {
  providers: [
    provideZoneChangeDetection({ eventCoalescing: true }),
    provideRouter(routes),
    graphqlProvider,
    provideHttpClient()
  ]
};
