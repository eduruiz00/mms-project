import gql from "graphql-tag";

export const FIRST_INGREDIENT = gql`
  query {
    ingredient {
      id
      name
    }
  }
`;