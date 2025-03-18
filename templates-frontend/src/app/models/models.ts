/** Succes type */
export interface ApiSuccess {
    __typename: "ApiSuccess"
    message: string
}

/** Error type */
export interface ApiError {
    __typename: "ApiError"
    message: string
}
