import { gql } from "apollo-angular";
import { TemplatesFragments } from "./fragments";
import { ApiSuccess } from "./models";

export const QUERY_SUCCESS_EXAMPLE = gql`
    query QuerySuccessExample {
        querySuccessExample {
            __typename
            ...ApiSuccessFragment
        }
    }
    ${TemplatesFragments.apiSuccess}
`

export interface ResponseQuerySuccessExample {
    querySuccessExample: ApiSuccess
}
