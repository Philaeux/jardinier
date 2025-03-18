import { gql } from "apollo-angular";
import { jardinierFragments } from "./fragments";
import { ApiSuccess } from "./models";

export const QUERY_SUCCESS_EXAMPLE = gql`
    query QuerySuccessExample {
        querySuccessExample {
            __typename
            ...ApiSuccessFragment
        }
    }
    ${jardinierFragments.apiSuccess}
`

export interface ResponseQuerySuccessExample {
    querySuccessExample: ApiSuccess
}
