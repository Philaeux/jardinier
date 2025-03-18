import { gql } from "apollo-angular";

export const TemplatesFragments = {
    apiError: gql`
        fragment ApiErrorFragment on ApiError {
            message
        }
    `,
    apiSuccess: gql`
        fragment ApiSuccessFragment on ApiSuccess {
            message
        }
    `
}
