import {PureComponent} from "react";
import {Link} from "react-router-dom";
import dateFormat from "dateformat";


/**
 * Заполнение ячеек пользователей
 */
export class UserItem extends PureComponent {

  render() {

    const {user, roles} = this.props;

    return (
      <tr>
        <td>
          <Link to={`/users/${user.id}`}>{user.username}</Link>
        </td>
        <td>
          {user.firstName}
        </td>
        <td>
          {user.lastName}
        </td>
        <td>
          {user.middleName}
        </td>
        <td>
          {user.email}
        </td>
        <td>
          {user.birthdate && dateFormat(user.birthdate, "fullDate")}
        </td>
        <td>
          {user.roles.map(
           (role_id, idx) =>
             <span key={idx}>
               {roles.find(role => role.id === role_id).role}
               <br/>
             </span>
          )}
        </td>
      </tr>
    )
  }
}